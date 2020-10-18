import os, sys
import customer

#while True:
email = input("Please enter your email:\n")   

try:
    user = customer.getProfile(email)
    print("Welcome", user['first_name'], user['last_name'])
except:
    print('Please try agian')
    sys.exit(0)    

while True:
    comm = input("Please enter command: ")
    if comm == 'q':
        os.system('pause')
        break
    elif (comm == 'address'):
        print(customer.getFullAddress(user['address_id']))
        os.system('pause')
        break
    else:
        print('Please try again')
        continue
