from socket import *

# Create and bind the server socket
s = socket(AF_INET, SOCK_STREAM)
s.bind(("", 8000))
s.listen(5)

print("================= ChatApp Server =================")
c, a = s.accept()  # Accept client connection
print(f"Connection established with {a}")

while True:
    data = c.recv(100).decode()  # Receive data from client
    print("<--", data)
    
    # Check if the client wants to end the chat
    if data.lower() == "bye" or data == "":
        print("Chat Ended by Client.")
        c.send("bye".encode('utf-8'))
        break
    
    # Input message to send to the client
    msg = input("--> ")
    c.send(msg.encode('utf-8'))

# Close the connection
c.close()
s.close()
