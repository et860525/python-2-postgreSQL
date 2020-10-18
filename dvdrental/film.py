import pandas as pd
from connection import connect
#TODO Create a table about bank
def getFilmTitle(title):
    rows = []
    sql = "SELECT title, rating, release_year, rental_rate FROM film WHERE title LIKE %s ORDER BY title"
    db_rows = connect.connect_fetchall(sql, title+'%')

    # If one columns only, output is ('Airplane Sierra',) not string
    #for row in db_rows:
    #    rows.append("".join(row))

    df = pd.DataFrame(db_rows, columns = ["title", "rating", "release_year", "rental_rate"])
    df.index += 1
    print(df)
    

if __name__ == "__main__":
    getFilmTitle('A')