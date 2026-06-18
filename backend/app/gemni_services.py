import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("You need a Gemini API key.")

client = genai.Client(api_key=api_key)


def generate_text(text: str, tone: str):
    prompt = f"""
You are a writing assistant.

Task: Fix grammar and improve clarity.

Tone: {tone}

Rules:
- Do NOT change meaning
- Only improve grammar and clarity
- Return only the final text

Text:
{text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text