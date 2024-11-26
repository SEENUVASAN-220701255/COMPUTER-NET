import sys
from socket import *

# Create UDP socket
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 55555))

print('UDP Echo Server ready')

while True:
    # Receive data from the client
    data, addr = s.recvfrom(1024)
    print(f"Server received {data.decode()} from {addr}")
    
    # Echo the data back to the client
    s.sendto(data, addr)
