from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your Vercel domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model and tokenizer
print("Loading SmolLM-135M model...")
MODEL_NAME = "HuggingFaceTB/SmolLM-135M"

# Check for CUDA availability
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME).to(device)

print(f"Model loaded successfully! Memory footprint: {model.get_memory_footprint() / 1e6:.2f} MB")

class VibeRequest(BaseModel):
    vibe: str

def get_vibe_guidance(vibe: str) -> str:
    """Get specific guidance for each vibe with examples"""
    vibe_patterns = {
        "romantic": """Generate a romantic and sweet pickup line that's genuine and heartfelt.
Example: 
Input: Generate a romantic pickup line
Output: Are you a magician? Because whenever I look at you, everyone else disappears. ❤️

Now generate a romantic pickup line: """,

        "cheesy": """Generate a super cheesy and over-the-top pickup line.
Example:
Input: Generate a cheesy pickup line
Output: Are you a parking ticket? Because you've got FINE written all over you! 😏

Now generate a cheesy pickup line: """,

        "nerdy": """Generate a nerdy, science-themed pickup line.
Example:
Input: Generate a nerdy pickup line
Output: Are you made of copper and tellurium? Because you're Cu-Te! 🔬

Now generate a nerdy pickup line: """,

        "cringe": """Generate the most cringey and over-the-top pickup line imaginable.
Example:
Input: Generate a cringe pickup line
Output: Are you a dictionary? Because you're adding meaning to my life! 📚

Now generate a cringe pickup line: """,

        "flirty": """Generate a bold and flirty pickup line.
Example:
Input: Generate a flirty pickup line
Output: Is your name Google? Because you've got everything I've been searching for! 😏

Now generate a flirty pickup line: """
    }
    return vibe_patterns.get(vibe, "Generate a pickup line with a ")

@app.post("/generate")
async def generate_pickup_line(request: VibeRequest):
    try:
        vibe = request.vibe
        vibe_guide = get_vibe_guidance(vibe)
        
        # Create the prompt
        prompt = f"""Instructions: Generate a pickup line with a {vibe} vibe.
{vibe_guide}"""
        
        # Prepare inputs
        encoded_input = tokenizer.encode_plus(
            prompt,
            return_tensors="pt",
            padding=True,
            return_attention_mask=True
        )
        input_ids = encoded_input["input_ids"].to(device)
        attention_mask = encoded_input["attention_mask"].to(device)
        
        # Generate response
        with torch.no_grad():
            outputs = model.generate(
                input_ids,
                attention_mask=attention_mask,
                max_new_tokens=100,
                do_sample=True,
                temperature=0.8,
                top_p=0.92,
                top_k=50,
                pad_token_id=tokenizer.eos_token_id,
                eos_token_id=tokenizer.eos_token_id,
            )
        
        # Get the full generated text
        full_response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Extract just the pickup line
        if full_response.startswith(prompt):
            response = full_response[len(prompt):].strip()
        else:
            response = full_response.replace(prompt, "").strip()
        
        # Clean up the response
        for marker in ["Instructions:", "Generate a pickup line:", "\n"]:
            if marker in response:
                response = response.split(marker, 1)[0].strip()
        
        # Add appropriate emoji based on vibe
        if vibe == "romantic":
            response += " ❤️"
        elif vibe == "cheesy":
            response += " 😏"
        elif vibe == "nerdy":
            response += " 🔬"
        elif vibe == "cringe":
            response += " 😂"
        elif vibe == "flirty":
            response += " 💋"
        
        return {"pickupLine": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 