# server.py
import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

def main():
    print("[STARTING] Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print("[LISTENING] Server is waiting for connections...")

    while True:
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")
        
        filename = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving filename: {filename}")
        conn.send("Filename received.".encode(FORMAT))
        
        with open(filename, "wb") as file:
            data = conn.recv(SIZE)
            print(f"[RECV] Receiving file data.")
            file.write(data)
        conn.send("File data received".encode(FORMAT))
        
        print(f"[DISCONNECTED] {addr} disconnected.")
        conn.close()

if __name__ == "__main__":
    main()
