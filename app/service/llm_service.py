import random
import time
import json
from google import genai
from app.config import Config

client = genai.Client(api_key=Config.API_KEY)

def extract_with_llm(text, max_retry=5):
    prompt = f"""
    Extract invoice data into JSON:
    vendor_name, invoice_number, date, vat_amount, total_amount, items

    TEXT:
    {text[:4000]}
    """

    for attempt in range(max_retry):
        try:
            response = client.models.generate_content(
                model="models/gemini-2.5-flash",
                contents=prompt
            )

            clean = response.text.replace("```json", "").replace("```", "").strip()
            return json.loads(clean)

        except Exception as e:
            wait_time = (2 ** attempt) + random.uniform(0.5, 1.5)

            print(f"[Retry {attempt+1}] error: {e}")
            print(f"Sleeping {wait_time:.2f}s...")

            time.sleep(wait_time)

    return None