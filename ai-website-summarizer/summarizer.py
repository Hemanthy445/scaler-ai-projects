import os
from openai import OpenAI
from dotenv import load_dotenv
from scraper import fetch_website_contents

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found. Please add it to your .env file.")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",
)

system_prompt = """You analyze the contents of a website and
give a short, friendly summary. Ignore navigation menus.
Respond in markdown."""

def summarize(url):
    website = fetch_website_contents(url)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # ← free Groq model
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Summarize this website:\n\n{website}"},
        ],
    )
    return response.choices[0].message.content