def login():
    print("--------------------")
    print("=== Login System ===")
    print("--------------------")

    username="iRony"
    password="ak47"

    input_user=input("Enter your username :")
    input_pass=input("Enter your password :")

    if input_user==username and input_pass==password:

        print ("Redirecting....")
    else:
        print("Username or password is incorrect.")

login()