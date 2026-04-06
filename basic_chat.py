from api import create_client

client = create_client(max_tokens=200)

while True:
  user_input = input("> ")
  answer = client.chat(user_input)

  print(answer)

