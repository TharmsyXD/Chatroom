import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message == 'USERNAME':
                client_socket.send(username.encode())
            else:
                print(message)
        except:
            print("Disconnected from the server.")
            client_socket.close()
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input("Enter the server IP address: ")
    port = int(input("Enter the server port number: "))
    global username
    username = input("Enter your username: ")

    client_socket.connect((host, port))

    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    while True:
        message = input('')
        if message == '/disconnect':
            break
        client_socket.send(message.encode())
    client_socket.close()

start_client()
