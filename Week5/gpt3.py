import os
import openai
from dotenv import load_dotenv, dotenv_values # use pip3 install python-dotenv

def callGPT3(promptString, tempVal, freqVal, presenceVal,  bestVal):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=promptString,
    temperature=tempVal,
    max_tokens=280,
    top_p=1,
    frequency_penalty=freqVal,
    presence_penalty=presenceVal,
    best_of = bestVal
  )
  return response

load_dotenv()  # take environment variables from .env.
SECRET_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = SECRET_KEY
current_response = callGPT3("Write a tweet poem about computers with legs and toes", 1.0, 1.0, 1.0, 5)


print(current_response)