def validate_user(name, email, password):

    if validate_name(name) == False:
        raise ValueError("Please make sure your name is greater than 2 characters!")

    if validate_email(email) == False:
        raise ValueError("Your email address is in the incorrect format, please enter a valid email.")

    if validate_password(password) == False:
        raise ValueError("Your password is too weak, ensure that your password is greater than 8 characters, and contains a capital letter and a number.")

    return True

def register_user(name, email, password):
    try: 
        validate_user(name, email, password)
    except:
         return False

    user = {
        "name": name,
        "email": email,
        "password": password
    }
    return user
