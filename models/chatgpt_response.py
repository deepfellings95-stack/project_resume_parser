import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

class chatGPTResponse:
    def __init__(self, text):
        self.text = text
        self.prompt = f"""
Extract structured resume information in JSON format.

Fields:
- name
- email
- phone
- skills (list)
- education (list)
- experience (list)

Resume:
\"\"\"{self.text}\"\"\"
IMPORTANT:
- Return ONLY valid JSON.
- Do NOT wrap the JSON in ```json``` or any code fences.
- No explanation, no text before or after.
"""

    def get_response(self):
        try:
            key = os.getenv("OPENRouter_CHATGPT_KEY")
            if not key:
                return {"error": "NO_OPENROUTER_KEY"}

            url = "https://openrouter.ai/api/v1/chat/completions"

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {key}",
            }

            payload = {
                "model": "openai/gpt-oss-20b:free",
                "messages": [
                    {"role": "user", "content": self.prompt}
                ]
            }

            response = requests.post(url, headers=headers, json=payload)
            data = response.json()

            # Extract the assistant content only
            final_output = data["choices"][0]["message"]["content"]

            return final_output

        except Exception as e:
            return {"error": str(e)}










                    
