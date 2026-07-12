import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("🔐 Welcome to the Password Generator!")
length = int(input("Enter the desired password length: "))
print("Your secure password is:", generate_password(length))
