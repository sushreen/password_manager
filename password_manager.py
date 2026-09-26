import random
import string

password = {}

#load password file
try:
    with open ("passwords.txt" , "r") as file:
        for line in file:
            website , pwd = line.strip().split(":")
            password[website] = pwd
except FileNotFoundError:
    pass

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

while True:
    print("\n----------PERSONAL PASSWORD MANAGER----------")
    print("1. Save a new password")
    print("2. View a password")
    print("3. Generate a random password")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        website = input("Enter website name:")
        pwd = input("Enter password:")
        password[website] = pwd

        with open("passwords.txt", "a") as file:
            file.write(f"{website}:{pwd}\n")

        print("Password saved successfully!")

    elif choice == "2":
        if not password:
            print("No passwords saved yet.")
        else:
            for website, pwd in password.items():
                print(f"Website: {website}, Password: {pwd}")

    elif choice == "3":
        print("Generated password:", generate_password())

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again. Bye ")
        break
else:
    print("Invalid choice. Please try again.")