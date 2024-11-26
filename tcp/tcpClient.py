import socket

clientfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
clientfd.connect(('localhost', 55555))  # Connect to the TCP server at localhost and port 55555

message = input("Enter your message: ")
clientfd.send(bytes(message, 'utf-8'))  # Send the message to the server

reply = clientfd.recv(1024).decode()  # Receive and decode the server's response
print("Message Received from Server: ", reply)

clientfd.close()
