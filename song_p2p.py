import os
import socket
import sys
import threading

from sqlite_lib import UsingSqlite


def send_file(file_path, client_socket):
    with open(file_path, "rb") as file:
        chunk = file.read(1024)
        while chunk:
            client_socket.send(chunk)
            chunk = file.read(1024)
    client_socket.close()


def broadcast_file(file_path, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", port))
    server_socket.listen(5)

    print(f"Broadcasting file: {file_path}")

    while True:
        client_socket, client_addr = server_socket.accept()
        print(f"Connected to {client_addr}")
        threading.Thread(target=send_file, args=(file_path, client_socket)).start()
        choice = input("Please enter a number to select an action:")

        if choice == "1":
            print("program continues...")
        elif choice == "2":
            print("The program exits.")
            sys.exit()
        else:
            print("Invalid input, program continues...")


def download_file(file_path, host, port):
    download_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    download_socket.connect((host, port))

    with open(file_path, "wb") as file:
        chunk = download_socket.recv(1024)
        while chunk:
            file.write(chunk)
            chunk = download_socket.recv(1024)

    download_socket.close()
    print(f"File downloaded: {file_path}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python song_p2p.py <mode> <file_path> <port>")
        sys.exit(1)

    mode = sys.argv[1]
    file_path = sys.argv[2]
    port = int(sys.argv[3])

    if mode == "broadcast":
        broadcast_file(file_path, port)
    elif mode == "download":
        host = input("Enter the host IP address: ")
        download_file(file_path, host, port)
    else:
        print("Invalid mode. Use 'broadcast' or 'download'.")