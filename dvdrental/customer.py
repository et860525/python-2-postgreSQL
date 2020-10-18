from connect import connect

def getProfile(email):
    sql = """SELECT customer_id, first_name, last_name, address_id FROM customer WHERE email = %s"""
    row = connect(sql, email)
    profile_key = ['customer_id', 'first_name', 'last_name', 'address_id']
    row = dict(zip(profile_key, row))
    
    return row
    
def getFullAddress(address_id):
    address = []

    # address
    sql = "SELECT address, city_id FROM address WHERE address_id = %s"
    row = connect(sql, address_id)
    address.append(row[0])   

    # city
    sql = "SELECT city, country_id FROM city WHERE city_id = %s"
    row = connect(sql, row[1])
    address.append(row[0])

    # country
    sql = "SELECT country FROM country WHERE country_id = %s"
    row = connect(sql, row[1])
    address.append(row[0]) 

    # combine to string
    address = "Address is %s, %s, %s" % (address[0], address[1], address[2])
    return address
    
    
