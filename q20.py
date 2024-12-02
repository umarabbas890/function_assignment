# Create a function to generate a random password of given length, containing uppercase, lowercase, numbers, 
# and special characters.
import random
import string

def generate_password(length):
    if length < 4:
        return "Password length must be at least 4 to include all character types."

    # Define character groups
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password includes at least one character of each type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special),
    ]

    # Fill the rest of the password with random characters from all groups
    all_characters = lowercase + uppercase + digits + special
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to make it random
    random.shuffle(password)

    # Return the password as a string
    return ''.join(password)

# Example usage
length = int(input("Enter the desired password length: "))
print("Generated password:", generate_password(length))
