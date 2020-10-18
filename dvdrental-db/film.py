import pandas as pd
from connect import connect, connect_fetchall

def getFilmTitle(title):
    rows = []
    sql = "SELECT title, rating, release_year, rental_rate FROM film WHERE title LIKE %s ORDER BY title"
    db_rows = connect_fetchall(sql, title+'%')

    # If one columns only, output is ('Airplane Sierra',) not string
    #for row in db_rows:
    #    rows.append("".join(row))

    df = pd.DataFrame(db_rows, columns = ["title", "rating", "release_year", "rental_rate"])
    df.index += 1
    print(df)
    