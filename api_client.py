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

print("quote")
print(quote)

print("author:")
print(author)



