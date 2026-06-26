# pandas for table creations
import pandas as pd
# retrieves & saves to db
import sqlalchemy as db
engine = db.create_engine("sqlite:///moodlift.db")

def create_tables():
    with engine.connect() as connection:
      connection.execute(db.text("""
        CREATE TABLE IF NOT EXISTS favorites (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          type TEXT,
          content TEXT,
          author TEXT
        );"""
      ))
      connection.commit()

# dictionary format
def save_favorite(item_type, content, author=""):
  favorite_dict = {
    "type": [item_type],
    "content": [content],
    "author": [author]
  }

  # convert dictionary to pandas dateframe
  df = pd.DataFrame.from_dict(favorite_dict)

  # date frame format to sql table
  df.to_sql(
    "favorites",
    con=engine,
    if_exists="append",
    index=False
  )

def view_favorites():
  try:
      df = pd.read_sql_query("SELECT * FROM favorites;", con=engine)
      if df.empty:
        print("Your saved list is empty.")
      else:
          print("+------------------------------------------------------+")
          print("|                   YOUR FAVORITES                     |")
          print("+------------------------------------------------------+")
          print(df[["type", "content", "author"]].to_string(index=False))
          print("+------------------------------------------------------+")
  except Exception:
      print("No favorites found yet! Save something first.")

      # print(pd.DataFrame(result))

create_tables()

print("Table created successfully!")