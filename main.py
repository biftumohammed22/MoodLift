from api_client import get_quote

def main():
  while True:
    print("Welcome to Moodlift")
    print("1.get a quote")
    print("2.Exit")

    choice = input("choose an option:")

    if choice == "1":
       quote, author = get_quote()
       print('Here is the quote:')
       print({quote})
       print("-{author}")
  
    elif choice == "2":
       print("Goodbye!")
       break
    else:
       print("invalid choice")

# 1. start the program
main()