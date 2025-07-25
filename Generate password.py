import random
import string

print("🔐 Welcome to the Password Generator!")

# Get user input for password length
try:
    length = int(input("Enter the desired password length: "))
except ValueError:
    print("Invalid input! Please enter a number.")
    exit()

# Ask user for complexity
include_letters = input("Include letters? (y/n): ").lower() == 'y'
include_digits = input("Include digits? (y/n): ").lower() == 'y'
include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

# Build the character set
characters = ''
if include_letters:
    characters += string.ascii_letters
if include_digits:
    characters += string.digits
if include_symbols:
    characters += string.punctuation

# Check if at least one type is selected
if not characters:
    print("You must select at least one character type!")
    exit()

# Generate password
password = ''.join(random.choice(characters) for _ in range(length))

print(f"\n✅ Your Generated Password: {password}")
