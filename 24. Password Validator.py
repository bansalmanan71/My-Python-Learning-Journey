print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("This is a program to validate whether a password is secure or not by using simple checks like: ")
print(">> Password should be atleast 8 characters long.")
print(">> Password should contain alphabets, numbers and special characters.")
print(">> Password should contain atleast one uppercase letter and atleast one lowercase letter.")
print()
password=input("Enter your desired password: ")

if len(password)<8:
    print("Your password is unsafe because your password length is less than 8 characters.")


for i in range(0,len(password)):
    # if password[i].isdigit():
    # We can use .isdigit method or we can have control in our hand by using the more native method.
    # if password[i] in ["0","1","2","3","4","5","6","7","8","9"]:
    if password[i] in "0123456789":
    # "0123456789" is a single string while ["0","1","2","3","4","5","6","7","8","9"] is a list of string, finding the character in a single string is cleaner.
        break
else:
    print("Your password is unsafe because your password does not contain any digits.")




for i in range(0,len(password)):
    if password[i].isalpha():
        break

else:
    print("Your password is unsafe because your password does not contain any alphabets.")

if any(char.isalpha() for char in password):
    for j in range(0,len(password)):
        if password[i].isupper():
            break
    else:
                print("Your password is unsafe because your password does not contain any upper case alphabets.")

if any(char.isalpha() for char in password):
    for j in range(0,len(password)):
        if password[i].islower():
            break
    else:
        print("Your password is unsafe because your password does not contain any lower case alphabets.")




# Mandating whitespace in passwords is not necessary, but if we had to, this is the way!
# for i in range(0,len(password)):
#      if password[i].isspace():
#           break
# else:
#      print("Your password is unsafe because your password does not contain whitespaces.")



# alnum checks alpha or num, not alpha and num
for i in range(0,len(password)):
     if not password[i].isalnum() and not password[i].isspace():
          break
else:
     print("Your password is unsafe because your password does not contain any special characters.")



if password[0]==" " or password[-1]==" ":
     print("Dear User, This is a gentle reminder that your password is starting or ending with a whitespace, which might have not been intended by you.")



    # Things i need to work upon
    # dont print upper case and lower case msg if the password do not even have alpha --> Completed
    # make it sequential using while loop and if user made a mistake then reenter the password and run the whole verification again until the user gets the password right