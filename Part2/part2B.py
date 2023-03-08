# # # # # # # # # # #
# Name: Oscar Bruno #
#   & Jacobo Fliman #
# Lab 2 Part 2      #
# Node B Code       #
# Due Date: 3-10-23 #
# # # # # # # # # # #

import socket
import sys
import binascii
import struct
import random

#Hardcoding IP address and port to forward to C
IP = "127.0.0.1"
forwardPort = 4000

#Function to calculate CRC32 
def crc32(v):
    return binascii.crc32(v.encode())

#Ask user for port to receive from A
if len(sys.argv) != 2:
    print("Useage: python " + sys.argv[0] + " <liseten port>")
    sys.exit(-1)

#create and bind socket struct
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((IP, int(sys.argv[1])))

print(f"Waiting for client at port: {sys.argv[1]}")

while True:
    #receive data from A
    data, addr = s.recvfrom(1024)
    print(f"Received message from: {addr} ")
    
    #unpack the data received from A into the string and crc32
    str,crc = struct.unpack("!50sL",data)
    
    #decode the string 
    str = str.decode("utf-8").replace("\0","")
    #print("str:%s\ncrc:%X" % (str,crc & 0xffffffff))
    
    #if the string is bye, send it to C, and close the socket, exit while loop
    #placed here so that it is not changed by the random number, and C is able to close without error
    if str == "bye":
        ss = struct.pack("!50sL",str.encode(),crc)
        s.sendto(ss,(IP, forwardPort))
        print("Socket closed")
        break
    
    #generate a random number between 0 and 9, if the number is less than 4, it changes the string received from A
    #this makes a 40% chance to change the message
    if random.randint(0,9) < 4:
        str = "Switched :)"
    
    #repacks the struct with the string (either original or changed one), and the CRC
    ss = struct.pack("!50sL",str.encode(),crc)
    
    #sends the new struct to C
    s.sendto(ss,(IP, forwardPort))
    