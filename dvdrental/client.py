import os, sys
import customer, film

#while True:
email = input("Please enter your email:\n")   

try:
    user = customer.getProfile(email)
    print("Welcome", user['first_name'], user['last_name'])
except:
    print('Please try agian')
    sys.exit(0)    

while True:
    comm = input("Please enter command(address, film, (q)uit): ")
    if comm == 'q':
        os.system('pause')
        break
    elif (comm == 'address'):
        print(customer.getFullAddress(user['address_id']))
        os.system('pause')
        break
    elif (comm == 'film'):
        while True:
            film_comm = input("Please enter command((t)itle, (c)ategory, (l)anguage): ")
            if (film_comm == 't'):
                film_title = input("Input film title: ")
                film.getFilmTitle(film_title)
                os.system('pause')
            elif (film_comm == 'c'):
                print('category')
            elif (film_comm == 'l'):
                print('language')
            elif (film_comm == 'q'):
                break
            else:
                print('Please try again')
                continue
    else:
        print('Please try again')
        continue
