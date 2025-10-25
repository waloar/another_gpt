
def OpenFile(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content_as_string = file.read()
        print("File content successfully read into a string:")
        print(file_content_as_string)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return file_content_as_string



from openai import OpenAI
client = OpenAI()

string_input = OpenFile("/Users/waltervodeb/Documents/Stanford/CoreNLP/docs/texto_1.txt")

response = client.responses.create(
  prompt={
    "id": "pmpt_68fd011996108197b5cf31467ce43e4f04844f18c0b88f21",
    "version": "2"
  },
  input=string_input,
  reasoning={},
  store=True,
  include=[
    "reasoning.encrypted_content",
    "web_search_call.action.sources"
  ]
)

print(response.output_text)


