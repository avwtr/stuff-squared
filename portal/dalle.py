import openai
from PIL import Image
import requests
import os
from dotenv import load_dotenv
#load_dotenv()

openai.api_key = os.environ.get('OPENAI_API_KEY')

def img_gen(prompt):
    response = openai.Image.create(
            prompt = prompt, n =1, size = "512x512"
            )
    resp_url = response["data"][0]["url"]
    image = Image.open(requests.get(resp_url, stream = True).raw)
    return image