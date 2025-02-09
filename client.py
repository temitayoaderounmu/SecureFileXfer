# client.py
import socket
from cryptography.fernet import Fernet

# Server Configuration
IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

# File Menu Options
menu_options = {
    1: "samp.txt",
    2: "samp1.txt",
    3: "samp2.txt",
    4: "Exit",
}

def print_menu():
    print("File Transfer Menu:")
    for key, value in menu_options.items():
        print(f"{key} -- {value}")

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()

def encrypt_file(key, input_file, output_file):
    cipher = Fernet(key)
    with open(input_file, "rb") as file:
        encrypted_data = cipher.encrypt(file.read())
    with open(output_file, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(key, input_file, output_file):
    cipher = Fernet(key)
    with open(input_file, "rb") as file:
        decrypted_data = cipher.decrypt(file.read())
    with open(output_file, "wb") as file:
        file.write(decrypted_data)

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    # Key Management
    key = generate_key()
    key = load_key()

    print_menu()
    try:
        option = int(input("Enter your choice: "))
        if option not in menu_options:
            raise ValueError("Invalid option. Please enter a number between 1 and 4.")
    except ValueError as e:
        print(e)
        return

    if option == 4:
        print("Exiting...")
        return

    filename = menu_options[option]
    encrypt_file(key, filename, "encrypted_file.txt")

    with open("encrypted_file.txt", "rb") as file:
        data = file.read()

    client.send("encrypted_file.txt".encode(FORMAT))
    print(f"[SERVER]: {client.recv(SIZE).decode(FORMAT)}")
    client.send(data)
    print(f"[SERVER]: {client.recv(SIZE).decode(FORMAT)}")

    if input("Decrypt the file? (Yes/No): ").strip().lower() == "yes":
        decrypt_file(key, "encrypted_file.txt", "decrypted_file.txt")
        print("Decryption complete. Check decrypted_file.txt.")

    client.close()

if __name__ == "__main__":
    main()
