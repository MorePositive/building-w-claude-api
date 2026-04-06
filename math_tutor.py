from api import create_client

system_prompt = """
You are a patient math tutor. Do not directly
answer a student's question. Guide them to a solution step by step
"""

client = create_client(max_tokens=100, system_prompt=system_prompt)

while True:
  user_input = input("> ")
  answer = client.chat(user_input)

  print(answer)

