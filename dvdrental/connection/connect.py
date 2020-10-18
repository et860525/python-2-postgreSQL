import psycopg2
from connection.config import config

"""
    Give SQL syntax and arguments.
"""
def connect(sql, *args):
    conn = None
    try:
        params = config()
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

def connect_fetchall(sql, *args):
    conn = None
    try:
        params = config()
        #print('Connecting to the DVD database...\n')
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        cur.execute(sql, args)
        rows = cur.fetchall()

        cur.close()

        return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()
            #print('Database connection closed.')

def create_tables(commands):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        for command in commands:
            cur.execute(command)
        
        cur.close()

        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()