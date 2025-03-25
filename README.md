# 💖 Pickup Line Generator

### A modern web application that generates fun, clever, or cringey pickup lines using the SmolLM-135M model. Built with Next.js and TailwindCSS, it’s fast, simple, and doesn’t ghost you.

> ## **Tired of staring at a dating app, wondering what to say first?** Let AI do the flirting for you.

<img src="https://github.com/user-attachments/assets/19d218ae-5958-4106-a4a9-59798cbdee10" alt="Pickup Line Generator" width="700"/>

> ## Smooth, silly, or straight-up ridiculous — we’ve got a line for that.

<img src="https://github.com/user-attachments/assets/83c131e5-a4b3-40af-b526-1353b0a47fd5" width="700"/>

> ## Choose *your* vibe. Hit generate. Shoot your shot!

<img src="https://github.com/user-attachments/assets/b69f347d-1e4b-443f-a3e8-2727b3a397c2" width="400"/>

> # Have fun out there, and good luck scoring that date (or getting laid 😉)! You got this. 😎💖

---

## 🌟 Features

- Generate pickup lines with different vibes:
  - 💝 Romantic
  - 😏 Cheesy
  - 🔬 Nerdy
  - 😂 Cringe
  - 💋 Flirty
- Modern, responsive UI with beautiful animations
- One-click copy to clipboard
- Powered by SmolLM-135M model

## 🛠️ Tech Stack

- **Frontend**: Next.js 13+ with App Router
- **Styling**: TailwindCSS
- **Model**: SmolLM-135M (via Hugging Face Inference API)

## 🚀 Getting Started

### Prerequisites

- Node.js 18+
- Python 3.8+

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd pickup-line-generator
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm run dev
```

Visit `http://localhost:3000` to see the application.

## 🌐 Deployment to Hugging Face Spaces

1. Push your code to GitHub
2. Create a new Space on Hugging Face:
   - Choose "Next.js" as the SDK
   - Connect your GitHub repository
   - The environment variables are already configured in the repository

The application will automatically build and deploy.

## 📁 Project Structure

```
pickup-line-generator/
├── app/
│   ├── page.tsx           # Main page component
│   ├── layout.tsx         # Root layout
│   ├── globals.css        # Global styles
│   └── api/
│       └── generate/      # API route for generation
│           └── route.ts
├── lib/
│   └── model.ts          # Model integration
└── public/               # Static assets
```

## 🎯 Example Pickup Lines

Here are some examples of what the generator can create:

- 💝 **Romantic**: "Are you a magician? Because whenever I look at you, everyone else disappears."
- 🔬 **Nerdy**: "Are you made of copper and tellurium? Because you're Cu-Te!"
- 😏 **Cheesy**: "Are you a parking ticket? Because you've got FINE written all over you!"
- 😂 **Cringe**: "Are you a dictionary? Because you're adding meaning to my life!"
- 💋 **Flirty**: "Is your name Google? Because you've got everything I've been searching for!"

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built using SmolLM by Hugging Face
- Deployed on Hugging Face Spaces 
