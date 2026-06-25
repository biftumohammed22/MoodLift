from api_client import get_quote, get_joke

def main():
  while True:
    print("Welcome to Moodlift")
    print("1.get a quote")
    print("2.Exit")

    choice = input("choose an option:")

    if choice == "1":
       quote, author = get_quote()
       joke_setup, joke_punchline = get_joke()
       print('Here is the quote:')
       print({quote})
       print("-{author}")
       print("-" * 30) # A clean separator line :D

       # Printing the joke portion
       print("Here is a joke to make you smile:")
       print(f"Setup: {joke_setup}")
       print(f"Punchline: {joke_punchline}")
  
    elif choice == "2":
       print("Goodbye!")
       break
    else:
       print("invalid choice")

main()
