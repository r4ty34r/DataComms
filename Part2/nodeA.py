# # # # # # # # # # #
# Group: Oscar Bruno#
#      Jacobo Fliman#
# Lab 2 Part 1      #
# Node A Code       #
# Due Date: 3-12-23 #
# # # # # # # # # # #


# Importing socket module
import socket

# Sys provides variables for input/output control
import sys

# If the length of the command line args is not 3
if len(sys.argv) != 2:

    # Prompt how to execute
    print("Useage: python " + sys.argv[0] + " <ip> <listen port>")
    
    # Exit program 
    sys.exit(-1)

# Initializing socket object, INET = IPv4 , SOCK_DGRAM specifying UDP 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Main program loop
while True:

    # Prompt for input
    print("Enter a message to send: ")
    # text holds data
    text = sys.stdin.readline().strip()
    
    # Sending data through socket object
    s.sendto(text.encode(),(sys.argv[1],int(sys.argv[2])))

    print(f"\nData transmitted through socket to IP: {sys.argv[1]} at port {sys.argv[2]}")

    if text == "bye" or text == "Bye":
        break

print("\nLoop exited")

# Close socket
s.close()

print("\nSocket closed")
