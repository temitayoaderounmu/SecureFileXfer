# Secure File Transfer 🔐

## Overview

Secure File Transfer is a simple yet powerful Python-based encrypted file-sharing system using **Sockets** and **Cryptography** (Fernet encryption). This project enables secure transmission of files between a client and a server over a local network. 🚀

## Features 🎯

- **AES-based Encryption (Fernet)** 🔑
- **Secure File Transmission** 📂
- **Easy-to-Use Menu System** 📜
- **Client-Server Communication** 📡
- **Data Integrity Checks** ✅

## How It Works ⚙️

1. The **client** selects a file to send.
2. The file is **encrypted** before transmission.
3. The **server** receives the encrypted file.
4. Optionally, the client can **decrypt** the file after transmission.

## Installation 🛠️

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/secure-file-transfer.git
   ```
2. Navigate into the project directory:
   ```sh
   cd SecureFileXfer
   ```
3. Install dependencies:
   ```sh
   pip install cryptography
   ```

## Usage 🚀

### Start the Server:

```sh
python server.py
```

### Run the Client:

```sh
python client.py
```

## File Encryption & Decryption 🔏

- Files are encrypted **before transmission** and stored securely.
- Users can **decrypt** files after transmission if needed.

## Example Output 🖥️

```bash
[STARTING] Server is starting...
[LISTENING] Server is waiting for connections...
[NEW CONNECTION] ('192.168.1.2', 50510) connected.
[RECV] Receiving filename: encrypted_file.txt
[RECV] Receiving file data.
[DISCONNECTED] ('192.168.1.2', 50510) disconnected.
```

## Contributing 🤝

Feel free to fork this repo and enhance it! If you have improvements, open a pull request. 🚀

## License 📜

This project is licensed under the MIT License.

## Author ✨

Developed by **Temitayo Aderounmu** 👨‍💻

