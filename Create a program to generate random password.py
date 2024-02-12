
import random

import string



def generate_password(length=12):

    # Define characters to use in the password

    characters = string.ascii_letters + string.digits + string.punctuation

    

    # Generate password

    password = ''.join(random.choice(characters) for i in range(length))

    

    return password



if __name__ == "__main__":

    password_length = int(input("Enter the length of the password: "))

    password = generate_password(password_length)

    print("Generated Password:", password)



