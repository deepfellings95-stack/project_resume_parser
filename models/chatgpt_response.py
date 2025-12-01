import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Set environment variables for OpenRouter
os.environ["OPENAI_API_KEY"] = os.getenv("OPENRouter_CHATGPT_KEY")
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

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
- No explanation, no text before or after.
"""

    def get_response(self):
        try:
            client = OpenAI()  # no args needed
            response = client.chat.completions.create(
                model="openai/gpt-oss-20b:free",
                messages=[{"role": "user", "content": self.prompt}]
            )
            return response
        except Exception as e:
            return f" error {e}"
