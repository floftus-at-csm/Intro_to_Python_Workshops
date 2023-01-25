import os
import openai
from dotenv import load_dotenv, dotenv_values # use pip3 install python-dotenv

def callGPT3(promptString, numTokens, tempVal, freqVal, presenceVal,  bestVal):
  response = openai.Completion.create(
    model="text-babbage-001",
    prompt=promptString,
    temperature=tempVal,
    max_tokens=numTokens,
    top_p=1,
    frequency_penalty=freqVal,
    presence_penalty=presenceVal,
    best_of = bestVal
  )
  return response

load_dotenv()  # take environment variables from .env.
SECRET_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = SECRET_KEY
# if(temperature < 0):
#   prompt = 
current_response = callGPT3("WRITE AN INTRODUCTION OF AN ESSAY ABOUT QUANTOM PHYSICS", 200, 1.0, 1.0, 1.0, 5)


# print(current_response)
print(current_response["choices"][0]["text"])







import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-babbage-001",
  prompt="write the opening of a film about computers with legs\n\n\n\nIn a future world where computers are weightless and able to travel wherever they please, one team of brilliant young programmers sets out to single-handedly save the world.",
  temperature=0.98,
  max_tokens=566,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)