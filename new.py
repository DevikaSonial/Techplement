import time
import string

def random_number(seed, length):
    random_numbers = []
    for _ in range(length):
        seed = (seed * 3 + 7) % 97
        random_numbers.append(seed)
    return random_numbers


def generate_password(length,uppercase, lowercase, digits, special_symbol):
    characters =""
    if uppercase=="y":
        characters += string.ascii_uppercase
    if lowercase=="y":
        characters += string.ascii_lowercase
    if digits=="y":
        characters += string.digits
    if special_symbol=="y":
        characters += string.punctuation
    password = []
    seed = int(time.time() * 1000) % 97  

    random_numbers = random_number(seed, length)
    for num in random_numbers:
        password.append(characters[num % len(characters)])

    return ''.join(password)


length = int(input("Enter length of password:"))
u=input("Upper Case(y/n)?\n")
l=input("Lower Case(y/n)?\n")
d=input("Digits(y/n)?\n")
s=input("Special symbol(y/n)?\n")
     
password = generate_password(length,u,l,d,s)
print("Generated password:", password)