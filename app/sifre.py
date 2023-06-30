import random
import string


def is_strong_password(password):
    if not (
        len(password) >= 8 and
        any(char.islower() for char in password) and
        any(char.isupper() for char in password) and
        any(char.isdigit() for char in password) and
        any(char in string.punctuation for char in password)
    ):
        raise ValueError("Make sure it's at least 8 characters and including a number, special character and a lowercase letter.")
    return True

def get_password_from_user():
    password = input("Please enter a password: ")
    try:
        is_strong_password(password)
    except ValueError as e:
        print(e)
        suggestion = generate_password_suggestion()
        print(f"Here's a suggestion for a stronger password: {suggestion}")
        get_password_from_user()
    else:
        print("Password is strong!")
        print('Password successfully created!')

def choose_random_char(characters):
    index = random.randint(0, len(characters) - 1)
    return characters[index]

def generate_password_suggestion():
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    suggestion = ''
    suggestion += choose_random_char(uppercase_letters)
    suggestion += choose_random_char(lowercase_letters)
    suggestion += choose_random_char(digits)
    suggestion += choose_random_char(special_chars)

    # Geri kalan karakterleri rastgele seç
    chars = uppercase_letters + lowercase_letters + digits + special_chars
    for i in range(9):
        suggestion += choose_random_char(chars)

    # Önerinin karakterlerini karıştır
    suggestion = ''.join(random.sample(suggestion, len(suggestion)))

    return suggestion