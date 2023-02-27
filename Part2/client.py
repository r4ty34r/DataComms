# # # # # # # # # # #
# Name: Oscar Bruno #
# Lab 2 Part 1      #
# Client Code       #
# Due Date:         #
# # # # # # # # # # #


# Importing socket module
import socket

# Sys provides variables for input/output control
import sys

# If the length of the command line args is not 3
if len(sys.argv) != 3:

    # Prompt how to execute
    print("Useage: python " + sys.argv[0] + " <ip> <liseten port>")
    
    # Exit program 
    sys.exit(-1)

# Initializing socket object, INET = IPv4 , SOCK_DGRAM specifying UDP 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Main program loop
while True:

    # Prompt for input
    print("Input text:")
    # text holds data
    text = sys.stdin.readline().strip()
    
    # Sending data through socket object
    s.sendto(text.encode(),(sys.argv[1],int(sys.argv[2])))
    print(f"\nSent data through socket to: {sys.argv[1]} at port {sys.argv[2]}")
    if text == "bye":
        break
