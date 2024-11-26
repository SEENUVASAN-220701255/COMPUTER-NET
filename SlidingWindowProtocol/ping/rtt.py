import sys
from socket import *
import time

# Client configuration
#ECHO_PORT = 55555
#BUFSIZE = 1024
#HOST = "127.0.0.1"  # Replace with the actual server IP
ADDR = ("127.0.0.1", 55555)

# Create UDP socket
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 0))

print('UDP Echo Client ready. Type your messages below:')

while True:
    try:
        # Read user input
        msg = input("Enter message: ")
        if not msg:  # Exit on empty input
            break

        # Send message to the server
        start = time.time()  # Start RTT measurement
        s.sendto(msg.encode(), ADDR)

        # Receive the echoed message
        data, fromaddr = s.recvfrom(1024)
        end = time.time()  # End RTT measurement

        # Calculate and display RTT
        rtt = end - start
        print(f"Client received {data.decode()} from {fromaddr}")
        print(f"RTT = {rtt:.6f} seconds\n")
    except KeyboardInterrupt:
        print("\nClient exiting...")
        break

# Close the socket
s.close()
