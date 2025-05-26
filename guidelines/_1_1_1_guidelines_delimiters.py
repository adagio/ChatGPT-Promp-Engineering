# from openai import OpenAI
from groq import Groq
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

# OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
# OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')

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

text = f"""
You should express what you want a model to do by \ 
providing instructions that are as clear and \ 
specific as you can possibly make them. \ 
This will guide the model towards the desired output, \ 
and reduce the chances of receiving irrelevant \ 
or incorrect responses. Don't confuse writing a \ 
clear prompt with writing a short prompt. \ 
In many cases, longer prompts provide more clarity \ 
and context for the model, which can lead to \ 
more detailed and relevant outputs.
"""
prompt = f"""
Summarize the text delimited by triple backticks \ 
into a single sentence.
```{text}```
"""
response = get_completion(prompt)
print(response)