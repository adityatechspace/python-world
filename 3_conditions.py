age = int(input("Enter your age: "))

if age < 18:
    print("You are not eligible to vote.")

elif age == 18:
    print("Congratulations on becoming eligible to vote!")

else:
    print("You are eligible to vote.")


#Mini Project: Simple login System 

user_name = input("Enter your username:")
password = input("Enter your Password:")


if user_name == "admin" and password == "password1234":
    print("Login Successfull, Welcome Admin!")

else:
    print("Incorrect Username or Password. Please try again.")

