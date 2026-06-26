# access enviroment variables
import os
# import requests allows python communicate with website/api
import requests
from dotenv import load_dotenv
# load_dotenv reads variables from .env file
load_dotenv()


API_KEY = os.getenv("API_NINJAS_KEY")

HEADERS = {
  "X-Api-Key": API_KEY
}

if API_KEY:
  print("API key loaded successfully")
else:
  print ("API key not found")

def get_quote():
  url = "https://api.api-ninjas.com/v1/quotes"
  response = requests.get(
    url,
    headers=HEADERS
  )
  data =response.json()
  quote = data[0]["quote"]
  author = data[0]["author"]

  return quote, author

quote, author = get_quote()

def get_joke():
  url = "https://official-joke-api.appspot.com/jokes/random"
  try:
    response = requests.get(url)
    if response.status_code == 200:
      data = response.json()
      setup = data["setup"]
      punchline = data["punchline"]
      return setup, punchline
    else:
      return "Why do programmers wear glasses?", "Because they can't C#."
  except Exception:
    return "Why do programmers wear glasses?", "Because they can't C#."

if __name__ == "__main__":
    quote, author = get_quote()
    # print to cl to test code
    print("quote")
    print(quote)

    print("author:")
    print(author)