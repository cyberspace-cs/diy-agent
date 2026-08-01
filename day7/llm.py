import os
from openai import OpenAI
from config import load_config,get_model,get_base_url


_client: OpenAI | None = None

def _get_client()->OpenAI:
    global _client
    if _client is None:
        kwags:dict={
            "api_key":os.environ["OPENAI_API_KEY"],
        }
        base_url=get_base_url()
        if base_url:
            kwags["base_url"]=base_url
        _client=OpenAI(**kwags)
    return _client


def chat(messages: list[dict])->str:
    response = _get_client().chat.completions.create(
        model="deepseek-v4-flash",
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content