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
            "content": "Eres un asistente útil."
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
Debes expresar lo que quieres que haga un modelo \ 
proporcionando instrucciones lo más claras y \ 
específicas posible. \ 
Esto guiará al modelo hacia la salida deseada \ 
y reducirá las posibilidades de recibir respuestas \ 
irrelevantes o incorrectas. No confundas escribir un \ 
prompt claro con escribir un prompt corto. \ 
En muchos casos, los prompts más largos brindan más claridad \ 
y contexto al modelo, lo que puede llevar a \ 
respuestas más detalladas y relevantes.
"""
prompt = f"""
Resume el texto delimitado por tres comillas invertidas \ 
en una sola oración.
```{text}```
"""
response = get_completion(prompt)
print(response)
