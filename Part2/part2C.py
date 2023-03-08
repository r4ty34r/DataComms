# # # # # # # # # # #
# Name: Oscar Bruno #
#   & Jacobo Fliman #
# Lab 2 Part 2      #
# Node C Code       #
# Due Date: 3-10-23 #
# # # # # # # # # # #

import socket
import binascii
import struct

#Calculates the crc32 value of a given string
def crc32(v):
    return binascii.crc32(v.encode())


#Hardcoding IP and port address
IP = "127.0.0.1"
port = 4000

#socket creation and bind
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((IP, port))
print(f"Waiting for client at port: {port}")

while True:
    #receive data from node B
    data, addr = s.recvfrom(1024)
    print(f"Received message from: {addr} ")
    
    #unpacks the data received from node B into a string and the CRC
    str,crc = struct.unpack("!50sL",data)
    #decode the string received from B
    str = str.decode("utf-8").replace("\0","")
    
    #if the message is "bye", the socket is closed, and exits the while loop
    if str == "bye":
        print("Socket closed")
        break
    
    #compare the CRC received from B to the CRC calculated by inputting the received string into the CRC32 function
    #then tells the user if the message was changed by B or not
    if crc32(str) != crc:
        print("The message has been changed")
    else:
        print("The message is intact")
    