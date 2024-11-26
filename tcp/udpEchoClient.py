import socket
import sys

ECHO_PORT = 55555
BUFSIZE = 1024

host = "127.0.0.1"
addr = (host, ECHO_PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create a UDP socket
s.bind(('', 0))  # Bind to an ephemeral port for client

print('UDP echo client ready. Type your message below:')
while True:
    message = input()
    if not message:
        break
    s.sendto(message.encode(), addr)  # Send the message to the server
    data, fromaddr = s.recvfrom(BUFSIZE)  # Receive the echoed message
    print('Client received:', data.decode(), 'from', fromaddr)
