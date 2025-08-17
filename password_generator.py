import random
import string

def main():

    password = input("Enter your current password: ")
    password_check(password)
    
def password_check(password):
    
    if password.isalpha() or password.isnumeric():
        print("Output: Weak")
    elif password.isalnum():
        print("Output: Medium")
    elif any(not char.isalnum() for char in password):
        print("Output: Strong")
    
    generate_input = input("\nWould you like to generate a new password? (Y/N) ")

    if generate_input.upper() == "Y":
        generate_password()

def generate_password():

    number = int(input("\nHow many characters would you like in your password? (8-20) "))
    password = "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=number))

    print(f"\nHere is a randomly-generated password for you: \n{password}")

main()
