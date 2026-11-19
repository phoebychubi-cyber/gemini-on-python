import requests

class Gemini:
    def __init__(self, api_key, model=None):
        if not api_key:
          raise ValueError("API key is required")
        
        self.api_key = api_key
        self.model = model or "gemini-3.5-flash-lite"
        
    def ask(self, prompt):
        headers = {
          "Content-Type": "application/json",
          "x-goog-api-key": self.api_key
        }
        URL = (
          f"https://generativelanguage.googleapis.com/v1beta/"
          f"models/{self.model}:generateContent"
        )
        payload = {
        "contents": [
            {
              "parts": [
                {"text": prompt}
              ]
            }
          ]
        }
        response = requests.post(
          URL,
          headers=headers,
          json=payload,
          timeout=60
        )

        try:
          
          if response.status_code == "400":
              raise RuntimeError(f"Gemini API request failed: Invalid API KEY")
              
          response.raise_for_status()
          
          data = response.json()

          return data["candidates"][0]["content"]["parts"][0]["text"]
        except requests.RequestException as error:
          raise RuntimeError(f"Gemini API request failed: {error}") from error