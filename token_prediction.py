from json import loads
from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

system="""You are a language model token probability simulator.
When given a text prompt, predict the top most likely next tokens and assign
realistic probability percentages that sum to 1.0.
Return ONLY a valid JSON array, no markdown, no explanation.
Format: [["token1", "0.35"], ["token2", "0.20"], ...]""",

client = Anthropic(api_key=api_key)

def get_next_token_predictions(prompt: str, top_n: int = 8):
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=300,
        system="""You are a language model token probability simulator.
When given a text prompt, predict the top most likely next tokens and assign
realistic probability percentages that sum to 1.0.
Return ONLY a valid JSON array, no markdown, no explanation.
Format: [["token1", "0.35"], ["token2", "0.20"], ...]""",
        temperature=0.0,
        messages=[
            {"role": "user", "content": f'Prompt: "{prompt}"\nReturn top {top_n} tokens.'}
        ],
    )

    raw = response.content[0].text.strip()
    return loads(raw)

# Usage
result = get_next_token_predictions("How was your")
for token, prob in result:
    print(f"{float(prob)*100:.1f}%  {token}")
