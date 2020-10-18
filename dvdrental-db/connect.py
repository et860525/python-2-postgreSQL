import psycopg2
from config import config

params = config()

def connect(sql, *args):
    conn = None
    try:
        #print('Connecting to the DVD database...\n')
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        cur.execute(sql, args)
        row = cur.fetchone()

        cur.close()

        return row
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()
            #print('Database connection closed.')