# from openai import OpenAI
from groq import Groq
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def get_completion(prompt, model="llama3-70b-8192"):
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content

prompt = f"""
Generate a list of three made-up book titles along \ 
with their authors and genres. 
Provide them in JSON format with the following keys: 
book_id, title, author, genre.
"""
response = get_completion(prompt)
print(response)
