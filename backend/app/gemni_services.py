import os
import time
from google import genai
from google.genai.errors import ServerError
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("You need a Gemini API key.")

client = genai.Client(api_key=api_key)

# Order best quality/fit first
MODELS = [
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite"
]


class GeminiBusyError(Exception):
    """Raised when all Gemini model attempts fail due to overload or temporary service issues."""
    pass


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


    for model_name in MODELS:
        for attempt in range(2):   # try each model 2 times
            try:
                print(f"Trying model: {model_name} (attempt {attempt + 1}/2)")

                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt
                )

                if not response.text:
                    raise ValueError(f"{model_name} returned an empty response.")

                return response.text

            except ServerError as e:
                last_error = e
                print(f"{model_name} server error on attempt {attempt + 1}: {e}")

                if "503" in str(e) or "UNAVAILABLE" in str(e):
                    if attempt < 1:
                        time.sleep(2)
                        continue
                    break

                # If it's some other server error, stop trying this model and move on
                break

            except Exception as e:
                last_error = e
                print(f"{model_name} failed on attempt {attempt + 1}: {e}")
                break

    raise GeminiBusyError(
        "Gemini is currently busy or unavailable. Please try again in a moment."
    ) from last_error