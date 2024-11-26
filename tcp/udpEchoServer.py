import socket

ECHO_PORT = 55555
BUFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create a UDP socket
s.bind(('', ECHO_PORT))  # Bind to all available interfaces on port 55555
print('UDP echo server ready')

while True:
    data, addr = s.recvfrom(BUFSIZE)  # Receive data from client
    print('Server received:', data.decode(), 'from', addr)
    s.sendto(data, addr)  # Echo the message back to the client
