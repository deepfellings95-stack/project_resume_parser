import os
import requests

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
        key = os.getenv("OPENRouter_CHATGPT_KEY")
        if not key:
            return "no key"

        url = "https://openrouter.ai/api/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://your-app.render.com",
            "X-Title": "Resume Parser"
        }

        data = {
            "model": "openai/gpt-oss-20b:free",
            "messages": [{"role": "user", "content": self.prompt}]
        }

        try:
            res = requests.post(url, headers=headers, json=data, timeout=60)
            res_json = res.json()

        # Return ONLY the actual JSON output
        return res_json["choices"][0]["message"]["content"]
        except Exception as e:
            return {"error": str(e)}
