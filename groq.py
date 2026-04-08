from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("GROQ_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

conversation = []

def ask_groq(prompt) -> str:
    try:
        conversation.append({"role" : "user", "content" : prompt})
        response = client.responses.create(
            input=conversation,
            model="openai/gpt-oss-20b",
        )
        result = response.output_text
        conversation.append({"role" : "Akil", "content" : result})
        return result
    except Exception as e:
        return f"Error : {e}"

print(conversation)

print("Welcome to GROQ AI")
while True:
    input_prompt = input("Ask Something.. \n('q' -> quit 'c' -> clear) : ")
    if input_prompt.lower() == 'q':
        break
    if input_prompt.lower() == 'c':
        conversation[:] = conversation[:-1]
        print("history cleared!")
        continue
    else:
        response = ask_groq(input_prompt)
        print(response)

print("Bye..")