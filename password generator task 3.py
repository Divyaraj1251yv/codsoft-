import random
import string

def generate_password(length):
    if length < 1:
        return "Error: Password length must be at least 1."

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    print("Password Generator")
    
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
