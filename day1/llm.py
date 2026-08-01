import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    #Deepseek
    base_url="https://api.deepseek.com",
    )


def chat(messages: list[dict])->str:
    response = client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content


