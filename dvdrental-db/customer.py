import os
import psycopg2

from config import config

params = config()

def sqlPoc(cur, sql, *argument):
    cur.execute(sql, (argument))
    row = cur.fetchone()
    return row

def getProfile(email):
    conn = None
    try:
        print('Connecting to the DVD database...\n')
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        sql = """SELECT customer_id, first_name, last_name, address_id FROM customer WHERE email = %s"""

        cur.execute(sql, (email,))
        row = cur.fetchone()
        
        profile_key = ['customer_id', 'first_name', 'last_name', 'address_id']
        row = dict(zip(profile_key, row))
        #print(row)

        cur.close()

        return row
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()
            #print('Database connection closed.')

def getAddress(address_id):
    conn = None
    address = []
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        sql = "SELECT address, city_id FROM address WHERE address_id = %s"
        cur.execute(sql, (address_id,))
        row = cur.fetchone()
        
        address.append(row[0])   

        sql = "SELECT city, country_id FROM city WHERE city_id = %s"
        row = sqlPoc(cur, sql, row[1])

        address.append(row[0])

        sql = "SELECT country FROM country WHERE country_id = %s"
        address.append(sqlPoc(cur, sql, row[1])[0]) 
        #print(address)

        address = "Address is %s, %s, %s" % (address[0], address[1], address[2])
        
        return address
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

#while True:
email = input("Please enter your email:\n")   

#if email == "q":
#    os.system('pause')
#    break

customer = getProfile(email)
print("Welcome", customer['first_name'], customer['last_name'])

os.system('pause')

#comm = input("Please enter command: ")
#
#if comm == 'q':
#    os.system('pause')
#elif (comm == 'address'):
#    print(getAddress(customer['address_id']))
#    os.system('pause')


    
    
