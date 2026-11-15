
import string
import secrets

def generate_password():

    print("\n===== PASSWORD GENERATOR =====")

    try:
        length = int(input("Enter password length: "))

        if length <= 0:
            print("Password length must be greater than zero.")
            return

        characters = ""
        password = []

        # Choose character types
        uppercase = input("Include uppercase letters? (yes/no): ").lower()
        lowercase = input("Include lowercase letters? (yes/no): ").lower()
        numbers = input("Include numbers? (yes/no): ").lower()
        symbols = input("Include special characters? (yes/no): ").lower()

        if uppercase == "yes":
            characters += string.ascii_uppercase
            password.append(secrets.choice(string.ascii_uppercase))

        if lowercase == "yes":
            characters += string.ascii_lowercase
            password.append(secrets.choice(string.ascii_lowercase))

        if numbers == "yes":
            characters += string.digits
            password.append(secrets.choice(string.digits))

        if symbols == "yes":
            special = "!@#$%^&*()-_+=?"
            characters += special
            password.append(secrets.choice(special))

        if not characters:
            print("Please select at least one character type.")
            return

        if length < len(password):
            print("Password length is too short for selected options.")
            return

        # Generate remaining characters
        for i in range(length - len(password)):
            password.append(secrets.choice(characters))

        # Shuffle password characters
        secrets.SystemRandom().shuffle(password)

        final_password = "".join(password)

        print("\nYour generated password is:")
        print(final_password)

    except ValueError:
        print("Please enter a valid number.")

# Run program
generate_password()
