import hashlib

# словник для зберігання пар логін-пароль
users = {}

# функція для верифікації пароля
def verify_password(password, hash_value):
    return hash_value == hashlib.sha256(password.encode()).hexdigest()

# функція для шифрування пароля
def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# реєстрація користувача
def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    hash_value = encrypt_password(password)
    if username in users:
        print("User already exists")
    else:
        users[username] = hash_value
        print("User registered successfully")

# авторизація користувача
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users:
        if verify_password(password, users[username]):
            print("User authenticated successfully")
        else:
            print("Incorrect password")
    else:
        print("User does not exist")

# головна функція
def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()