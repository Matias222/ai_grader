import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key= os.getenv("OPENAI_API_KEY")

def grader(codigo_alumno: str):

    with open("prompt_grader.txt") as f: texto_f=f.read()
    
    prompt=texto_f.format(codigo_alumno)
    
    messages = [{"role" : "user", "content" : prompt}]

    result = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",
            messages=messages,
            temperature=0,
            )
        
    with open("correcion_francisco.txt", "w") as file: file.write(result["choices"][0]["message"]["content"])

    #print(result["choices"][0]["message"]["content"])
    return result["choices"][0]["message"]["content"]


with open("francisco_mauricio.txt") as f: 
    texto_f=f.read()
    grader(texto_f)