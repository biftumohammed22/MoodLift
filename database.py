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
  print(f"★ Successfully saved this {item_type} to favorites!")

def view_favorites():
  try:
    df = pd.read_sql_query("SELECT * FROM favorites;", con=engine)
    if df.empty:
        print("Your saved favorites list is empty.")
    else:
        pd.set_option('display.max_colwidth', 50)  # Fixing sizing error i Ran into with the CLI
        pd.set_option('display.width', 1000)

        print("================= YOUR SAVED FAVORITES =================")
        print(df[["id", "type", "content", "author"]].to_string(index=False))
        print("========================================================")
  except Exception:
    print("No favorites found yet! Save something first.")
  
def delete_favorite(favorite_id):
    with engine.connect() as connection:
        connection.execute(
            db.text("DELETE FROM favorites WHERE id = :id;"),
            {"id": favorite_id}
        )
        connection.commit()
    print(f" Successfully deleted favorite #{favorite_id}!")

create_tables()

print("Table created successfully!")