import random
import string

print("\n🔐 Welcome to the Advanced Password Generator 🔐")

# Get user input
length = int(input("📏 Enter the desired password length: "))
include_uppercase = input("🔠 Include uppercase letters? (yes/no): ").lower() == 'yes'
include_lowercase = input("🔡 Include lowercase letters? (yes/no): ").lower() == 'yes'
include_digits = input("🔢 Include digits? (yes/no): ").lower() == 'yes'
include_symbols = input("🔣 Include symbols? (yes/no): ").lower() == 'yes'

# Build the character set
characters = ""
if include_uppercase:
    characters += string.ascii_uppercase
if include_lowercase:
    characters += string.ascii_lowercase
if include_digits:
    characters += string.digits
if include_symbols:
    characters += string.punctuation

if not characters:
    print("❌ No character types selected. Please choose at least one type.")
else:
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"\n🔑 Your generated password: \033[1m{password}\033[0m")

    # Strength check
    strength = "Weak"
    if length >= 12 and include_uppercase and include_lowercase and include_digits and include_symbols:
        strength = "Strong 💪"
    elif length >= 8 and include_lowercase and include_digits:
        strength = "Moderate 🔐"

    print(f"🔎 Password Strength: {strength}")
