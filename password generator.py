import random
import string


def generate_password(length, complexity):
    # Character sets
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation

    # Ensuring the inclusion of different character types according to complexity
    if complexity == 'simple':
        characters = letters
        password = ''.join(random.choice(characters) for i in range(length))
    elif complexity == 'medium':
        characters = letters + digits
        password = ''.join(random.choice(characters) for i in range(length))
    elif complexity == 'strong':
        # Ensure at least one character from each type is included
        password_chars = [
            random.choice(letters),
            random.choice(digits),
            random.choice(punctuation)
        ]
        # Fill the rest of the length with random choices from the combined set
        for _ in range(length - len(password_chars)):
            password_chars.append(random.choice(letters + digits + punctuation))
        # Shuffle to avoid predictable patterns
        random.shuffle(password_chars)
        password = ''.join(password_chars)
    else:
        print("Invalid complexity selected. Generating a strong password by default.")
        characters = letters + digits + punctuation
        password = ''.join(random.choice(characters) for i in range(length))

    return password


print("Welcome to the Password Generator!")

# User input for length
try:
    length = max(int(input("Enter the desired length of the password: ")), 3)  # Ensure minimum length for 'strong'
except ValueError:
    print("Please enter a valid number.")
    exit()

# User input for complexity
print("\nChoose the complexity of the password:")
print("simple - Only letters (uppercase and lowercase)")
print("medium - Letters and digits")
print("strong - Letters, digits, and special characters/punctuation")
complexity = input("Your choice (simple/medium/strong): ").lower()

# Generate and display the password
password = generate_password(length, complexity)
print(f"\nYour new password is: {password}")
