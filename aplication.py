
import json
from openai import OpenAI


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


def save_file(data, filename, indent=4):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(data)
        algo = OpenFile(filename) 
        elJson = json.loads(algo)
        return elJson
        print(f"Data successfully saved to {filename}")
    except IOError as e:
        print(f"Error saving file {filename}: {e}")
    except TypeError as e:
        print(f"Error serializing data to JSON: {e}. Ensure all data types are JSON serializable.")



client = OpenAI()

string_input = OpenFile("/Users/waltervodeb/Documents/Stanford/CoreNLP/docs/train_partes_walter_1.txt")

response = client.responses.create(
  prompt={
    "id": "pmpt_68fd011996108197b5cf31467ce43e4f04844f18c0b88f21",
    "version": "8"
  },
  input=string_input,
  reasoning={},
  store=True,
  include=[
    "reasoning.encrypted_content",
    "web_search_call.action.sources"
  ]
)

if response:
    save_file(response.output_text, "response_output.json")

# print(response.output_text)


