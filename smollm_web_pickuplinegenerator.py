import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import gradio as gr
import re

# Set page title and description
title = "💖 Pickup Line Generator"
description = """
<div style="text-align: center; max-width: 650px; margin: 0 auto;">
  <div>
    <p>Generate fun, clever, or cringey pickup lines using SmolLM-135M! Select a vibe and click generate to get started! 😏</p>
  </div>
</div>
"""

# Load model and tokenizer
print("Loading SmolLM-135M model...")
MODEL_NAME = "HuggingFaceTB/SmolLM-135M"

# Check for CUDA availability
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
# Set pad_token to eos_token to handle padding
tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME).to(device)

print(f"Model loaded successfully! Memory footprint: {model.get_memory_footprint() / 1e6:.2f} MB")

def get_vibe_guidance(vibe):
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

def generate_pickup_line(vibe):
    """Generate a pickup line based on the selected vibe"""
    # Get the vibe guidance
    vibe_guide = get_vibe_guidance(vibe)
    
    # Create the prompt
    prompt = f"""Instructions: Generate a pickup line with a {vibe} vibe.
{vibe_guide}"""
    
    # Prepare inputs with explicit attention mask
    encoded_input = tokenizer.encode_plus(
        prompt,
        return_tensors="pt",
        padding=True,
        return_attention_mask=True
    )
    input_ids = encoded_input["input_ids"].to(device)
    attention_mask = encoded_input["attention_mask"].to(device)
    
    # Generate multiple responses and pick the best one
    num_tries = 3
    best_response = None
    
    for _ in range(num_tries):
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
        
        best_response = response
        break
    
    return best_response

# Create custom CSS
custom_css = """
.gradio-container {
    background-color: #fef6f9 !important;
}
.title {
    font-family: 'Lobster', cursive !important;
    color: #ff69b4 !important;
}
.button {
    background: linear-gradient(45deg, #ff69b4, #ff1493) !important;
    color: white !important;
    border: none !important;
    transition: all 0.3s ease !important;
}
.button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(255, 105, 180, 0.3);
}
"""

# Create the Gradio interface
with gr.Blocks(theme="soft", css=custom_css) as demo:
    gr.Markdown(f"# {title}")
    gr.Markdown(description)
    
    with gr.Row():
        with gr.Column():
            vibe_dropdown = gr.Dropdown(
                choices=[
                    "romantic",
                    "cheesy",
                    "nerdy",
                    "cringe",
                    "flirty"
                ],
                label="Pick a vibe",
                value="romantic"
            )
            generate_btn = gr.Button("Generate Line", elem_classes="button")
        
        with gr.Column():
            output = gr.Textbox(
                label="Your pickup line",
                lines=3,
                interactive=False
            )
            copy_btn = gr.Button("📋 Copy to Clipboard", elem_classes="button")
    
    # Example inputs
    gr.Examples(
        examples=[
            ["romantic"],
            ["cheesy"],
            ["nerdy"],
            ["cringe"],
            ["flirty"]
        ],
        inputs=[vibe_dropdown]
    )
    
    generate_btn.click(
        fn=generate_pickup_line,
        inputs=[vibe_dropdown],
        outputs=output
    )
    
    # Footer
    gr.Markdown("""
    <div style="text-align: center; margin-top: 20px; color: #666;">
        Built by Nath with SmolLM 🔥
    </div>
    """)

# Launch the app
if __name__ == "__main__":
    demo.launch(share=True)  # Set share=False if you don't want to create a public link
