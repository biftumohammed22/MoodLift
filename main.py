from api_client import get_quote, get_joke
from database import save_favorite, view_favorites, delete_favorite  #Imports the functions within the database.py file

def main():
  while True:
    print("+-----------------------+")
    print("|  WELCOME TO MOODLIFT  |")
    print("+-----------------------+")
    print("")
    print("Lift your mood with a quote and a joke!")
    print("----------------------------------------")
    print("")
    print("Please choose an option:")
    print(" 1. Get a quote")
    print(" 2. View/Manage Saved Favorites")
    print(" 3. Exit")

    choice = input("Choose an option:")

    if choice == "1":
       quote, author = get_quote()
       joke_setup, joke_punchline = get_joke()
       print('Here is the quote:')
       print(f"{quote}")
       print(f"- {author}")
       print("-" * 50) # A clean separator line :D

       # Printing the joke portion
       print("Here is a joke to make you smile:")
       print(f"Setup: {joke_setup}")
       print(f"Punchline: {joke_punchline}")

       save_choice = input("Would you like to save the (1) Quote, (2) Joke, or (3) Skip? ").strip()
       if save_choice == "1":
           # this willl save the quote string
           save_favorite("quote", quote, author)
       elif save_choice == "2":
           # this will save the joke
           full_joke = f"{joke_setup} -> {joke_punchline}"
           save_favorite("joke", full_joke, "Universal Joke API")

    elif choice == "2":
       view_favorites()
       manage_choice = input("Would you like to delete an item? (yes/no): ").strip().lower()
       if manage_choice == "yes" or manage_choice == "y":
           try:
               id_Delete = int(input("Enter the ID number of the item to delete: "))
               delete_favorite(id_Delete)
           except ValueError:
               print("Invalid input. Please enter a valid number ID.")

    elif choice == "3":
       print("+-----------------------+")
       print("|       Goodbye!        |")
       print("+-----------------------+")
       
       break
    else:
       print("Invalid choice")

main()
