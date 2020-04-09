import string
import random
print("HNG Tech Employee Register")

user_info=[]
database=[]

status=True
while status:
    first_name=input("Please enter your First Name: ")
    last_name=input("Please enter your Last Name: ")
    email=input("Provide Email Address: ")
    
    user_info= [first_name,last_name,email] #assigning values to list
    
    lenght=5 #lenght of randomly generated string 
    random.choice(string.ascii_lowercase)
    c="".join(random.choice(string.ascii_lowercase) for i in range(lenght))

    a= first_name[0:2]  #first 2 characters of first name
    b= last_name[-2:] #last two characters of last name

    password=a+b+c
    response = input(f"Your Password is: {password} \nDo you like it? Enter Yes/No: ")
    password_ok=True
    while password_ok: #while loop to confirm user likes generated password
        if response == "Yes":
            user_info.append(password)
            database.append(user_info)
            break
        else:
            user_password=input("Please enter preferred password(at least 7 characters): ")
            password_len=True
            while password_len: #while loop to confirm lenght of chosen password
                if len(user_password)<7:
                    password=input("Password must be at least 7 characters: ")
                    
                else:
                    user_info.append(user_password)
                    database.append(user_info)
                    break
    next_user=input("Will you like to add another user? Enter Yes/No: ")
    if next_user=="No":
        status=False
        for items in database:
            print(items)
    else:
        status=True