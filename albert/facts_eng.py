import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')


def facts(input_):
  response = openai.Completion.create(
    model="text-davinci-001",
    prompt=input_,
    temperature=0.4,
    max_tokens=64,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  final = response['choices'][-1]['text']
  return final