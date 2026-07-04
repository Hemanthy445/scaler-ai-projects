# LLM Arena

Send the same prompt to two different LLMs and vote on which answered better.
Inspired by LMSYS Chatbot Arena.

## Models
- GPT-OSS 120B (OpenAI open-source via Groq)
- Llama 3.1 8B (Meta via Groq)

## How it works
- `groq_call.py` — API calls for both models using OpenAI SDK pointed at Groq
- `arena.py` — battle() sends same prompt to both models
- `arena_app.py` — Gradio Blocks UI with side-by-side output and voting

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/Hemanthy445/scaler-ai-projects.git
cd scaler-ai-projects/llm-arena
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Get a free Groq API key
Sign up at https://console.groq.com — same key works for both models.

### 5. Create .env file
```bash
echo "GROQ_API_KEY=your-key-here" > .env
```

### 6. Run
```bash
python arena_app.py
```
Open http://127.0.0.1:7860 in your browser.