
import json
from agents import Agent, Runner
import os
from dotenv import load_dotenv
from pydantic import BaseModel

def OpenFile(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content_as_string = file.read()
            return file_content_as_string
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None


class ResearchPaperExtraction(BaseModel):
    es_documento_legal: str
    Fuero: str
    Materia: str
    Fuero: str
    Radicacion: str
    Resumen: str

env_path = os.path.join(os.path.dirname(__file__), 'deploy.env')
load_dotenv(dotenv_path=env_path)

string_input = OpenFile("docs/libra_mandamiento.txt")

agent = Agent(name="Legal Resume Tagger", instructions="Eres un asistente experto del derecho argentino. Debes determina si el texto escrito es un documento legal, Clasificalo segun su fuero (Civil, Comercial, Laboral, Administrativo, Tributario), determina la materia del reclamo, si es posible donde tramita (radicacion),  y haz un breve resumen de la peticion en una oracion sobre el texto. Tus respuesta debe estar en formato JSON con los siguiente campos: es_documento_legal (boolean), fuero (string), materia (string), radicacion (string), resumen (string). Si el texto no es legal setear la materia en  'N/A'. El resultado debe estar en el idioma origen del texto.",
                  output_type=ResearchPaperExtraction)

response = Runner.run_sync(agent, string_input)
if response:
    #json.dumps(response.final_output)
    print(response.final_output)
    # save_file(response.output_text, "response_output.json")

print(response.final_output)

# client = OpenAI()



# response = client.responses.create(
#   prompt={
#     "id": "pmpt_68fd011996108197b5cf31467ce43e4f04844f18c0b88f21",
#     "version": "8"
#   },
#   input=string_input,
#   reasoning={},
#   store=True,
#   include=[
#     "reasoning.encrypted_content",
#     "web_search_call.action.sources"
#   ]
# )

# if response:
#     resultado = json.loads(response.output_text)
#     print(resultado)
#     save_file(response.output_text, "response_output.json")



