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

IP = 127.0.0.1

# If the length of the command line args is not 3
if len(sys.argv) != 2:
    # Prompt execution instruction
    print("Useage: python " + sys.argv[0] + " <liseten port>")
    # Exit program
    sys.exit(-1)

# Initializing socket object
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Binding socket and IP address
s.bind((IP, int(sys.argv[1])))
print(f"Waiting for client on port: {sys.argv[1]} ")

# Main program loop
while True:

    # recvfrom returns a tuple with the data and addr 
    data, addr = s.recvfrom(1024)

    # Log client info
    print(f"Client connection: {addr} ")

    # Log data to console
    print(f"Message received: {data.decode()}")
    #print(data.decode("utf-8"))


    # Exit loop if connection is ended
    if data.decode("utf-8") == "bye" or data.decode("utf-8") == "Bye":
        print("\nConnection closed by client")
        break

print("\nLoop exited")

# Close socket 
s.close()

print("\nSocket closed")
