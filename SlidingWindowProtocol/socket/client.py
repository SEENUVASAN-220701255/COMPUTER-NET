from socket import *

# Create and connect the client socket
s = socket(AF_INET, SOCK_STREAM)
s.connect(("127.0.0.1", 8000))

print("================= ChatApp Client =================")
while True:
    # Input message to send to the server
    msg = input("--> ")
    s.send(msg.encode('utf-8'))
    
    # Receive reply from server
    data = s.recv(100).decode()
    print("<--", data)
    
    # Check if the server wants to end the chat
    if data.lower() == "bye" or data == "":
        print("Chat Ended by Server.")
        break

# Close the connection
s.close()
