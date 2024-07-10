from openai import OpenAI
import os

class OpenAIBot:
    def __init__(self, model):
        self.model = model
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")
        self.client = OpenAI(api_key=api_key)
        self.messages = []

    def generate_response(self, prompt):
        self.messages.append({"role": "user", "content": prompt})
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages
            )
            bot_response = response.choices[0].message.content
            self.messages.append({"role": "assistant", "content": bot_response})
            return bot_response
        except Exception as e:
            print(f"OpenAI API Error: {e}")
            return None