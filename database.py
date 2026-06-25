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
  df = pd.dateframe.from_dict(favorite_dict )

  # date frame format to sql table
  df.to_sql(
    "favorites",
    con=engine,
    if_exists="append",
    index=False
  )

  def view_favorites():
    with engine.connect() as connection:
      result = connection.execute(
        db.text("SELECT* FROM favorites;")
      ).fetchall()

      return result

      # print(pd.DataFrame(result))

create_tables()

print("Table created successfully!")