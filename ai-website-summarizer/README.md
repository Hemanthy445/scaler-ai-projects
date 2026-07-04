# AI Website Summarizer

Enter any website URL and get an AI-generated summary powered by Llama 3.3 70B via Groq (free).

## How it works
- `scraper.py` — fetches and cleans webpage content using requests + BeautifulSoup
- `summarizer.py` — sends content to Groq's Llama model with a summarization prompt
- `app.py` — serves a Gradio web UI

## Setup

### 1. Clone the repo
\`\`\`bash
git clone https://github.com/Hemanthy445/scaler-ai-projects.git
cd scaler-ai-projects/ai-website-summarizer
\`\`\`

### 2. Create virtual environment
\`\`\`bash
python -m venv venv
source venv/bin/activate
\`\`\`

### 3. Install dependencies
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Get a free Groq API key
Sign up at https://console.groq.com and create an API key.

### 5. Create .env file
\`\`\`bash
echo "GROQ_API_KEY=your-key-here" > .env
\`\`\`

### 6. Run
\`\`\`bash
python app.py
\`\`\`
Open http://127.0.0.1:7860 in your browser.
