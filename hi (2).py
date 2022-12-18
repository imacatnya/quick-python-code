#*********** BEGIN ACCOUNT CREATION ***************
msg = "Invalid entry. Try again."
print("Welcome to Python Account!")
while True:
    # ***** THIS BLOCK CREATES NEW USERNAME
    try:
        username = input("Create New Username: ") #create new username
    except ValueError:
        msg
    else:
        try:
            username2 = input("Confirm username: ") # confirm username
        except ValueError:
            msg
        else:
            if username2 != username: # if no match, try again
                print("Usernames do not match. Try again.")
                continue
            else:
                print("Username created!")
                
                #THIS BLOCK CREATES NEW PASSWORD
                while True:
                    try:
                        password = input("Create a new password: ")
                    except ValueError:
                        msg
                    else:
                        password2 = input("Confirm password: ")
                        if password2 != password:
                            print("Passwords don't match. Try again.")
                            continue
                        else:
                            print("Password created!")
                            break
                    break
    break
# ****************** END ACCOUNT CREATION ******************


# # ****************** BEGIN ACCOUNT LOGIN *****************
print("PLEASE LOG INTO YOUR ACCOUNT")
attempts = 5 # this will allow 5 attempts
while attempts > 0:
    attempts -= 1
    try:
        usrnm = input("Enter username: ")
        pwd = input("Enter password: ")
    except ValueError:
        msg
    else:
        if usrnm.isspace() or pwd.isspace():
            print("Space not allowed.")
            continue
        elif usrnm == '' or pwd == '':
            print("Value needed.")
            continue
        elif usrnm != username2 or pwd != password2:
            print("Credentials do not match. Try again.")
            print(f'You have {attempts} attempts left')

            if attempts == 0: # once user exhausts attempts, account is locked
                print("You have been locked out of your account")
                break
            continue

        else:
            print(f"Welcome {username2}!")
            break
    break
# *************** END ACCOUNT CREATION *************