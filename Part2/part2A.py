# # # # # # # # # # #
# Name: Oscar Bruno #
#   & Jacobo Fliman #
# Lab 2 Part 2      #
# Node A Code       #
# Due Date: 3-10-23 #
# # # # # # # # # # #

import socket
import struct
import sys
import binascii

#function that generates the CRC32
def crc32(v):
     r = binascii.crc32(v.encode())
     return r

#hardcoded IP address
IP = "127.0.0.1"

#get port from user
if len(sys.argv) != 2:
    print("Useage: python " + sys.argv[0] + " <listen port>")
    sys.exit(-1)
    
#create socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    #ask user to input text
    print("Input text:")
    text = sys.stdin.readline().strip()
    
    #makes a struct with the encoded input and the crc32 of that text, then sends it to the user
    ss = struct.pack("!50sL",text.encode(),crc32(text))
    s.sendto(ss,(IP,int(sys.argv[1])))
    if text == "bye":
        break
