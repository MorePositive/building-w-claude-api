from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

class ApiConfig:
    def __init__(self, model="claude-sonnet-4-5", max_tokens=500, system_prompt=None):
        self.client = Anthropic()
        self.model = model
        self.max_tokens = max_tokens
        self.system_prompt = system_prompt
        self.messages = []

    def create_client(**kwargs):
      return ApiConfig(**kwargs)
    
    def chat(self, user_message):
        self.messages.append({"role": "user", "content": user_message})

        params = {
            "model": self.model,
            "max_tokens": self.max_tokens,
            "messages": self.messages
        }
        if self.system_prompt:
            params["system"] = self.system_prompt

        response = self.client.messages.create(**params)
        assistant_message = response.content[0].text
        self.messages.append({"role": "assistant", "content": assistant_message})

        return assistant_message

create_client = ApiConfig
