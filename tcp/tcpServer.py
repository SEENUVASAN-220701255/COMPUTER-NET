import socket

sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
print('Socket Created')

sockfd.bind(('localhost', 55555))  # Bind to localhost and port 55555
sockfd.listen(3)  # Start listening for up to 3 clients
print('Waiting for connections')

while True:
    clientfd, addr = sockfd.accept()  # Accept a client connection
    print("Connected with ", addr)
    receivedMsg = clientfd.recv(1024).decode()  # Receive message from client
    print("Message Received from Client: ", receivedMsg)

    clientfd.send(bytes(receivedMsg, 'utf-8'))  # Echo the message back
    print("Message reply sent to Client!")
    
    print("Do you want to continue (type y or n):")
    choice = input().strip().lower()
    if choice == 'n':
        break

sockfd.close()
