# # # # # # # # # # #
# Name: Oscar Bruno #
# Lab 2 Part 1      #
# Server Code       #
# Due Date:         #
# # # # # # # # # # #

# Importing socket module
import socket

# Sys provides variables for input/output control
import sys


# If the length of the command line args is not 3
if len(sys.argv) != 2:
    # Prompt execution instruction
    print("Useage: python " + sys.argv[0] + " <liseten port>")
    # Exit program
    sys.exit(-1)

# Initializing socket object
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Binding socket and IP address
s.bind(("0.0.0.0", int(sys.argv[1])))
print(f"Waiting for client on port: {sys.argv[1]} ")

# Main program loop
while True:

    # recvfrom returns a tuple with the data and addr 
    data, addr = s.recvfrom(1024)

    # Log data to console
    print(data.decode("utf-8"))

    # Exit loop if connection is ended
    if data.decode("utf-8") == "bye":
        break
