# Lab 1 - Client program
# Due date: 2-17-23
# Oscar Bruno

# Initializing socket 
import socket

client = socket.socket()
portnum = 9000

#connection
client.connect(('localhost',portnum))  

# specifying size of data
buf = 1024

while (True):
    msg = "Hello Fordham"
    if len(msg) == 0 :continue

    # send data
    client.send(msg.encode())  

    #accept a message back 
   #client.accept() 

    # receive data
    #data = client.recv(buf)    

    #print(data.decode())

    # receiving message back from server
    #secondmsg = client.recv(buf)
    
    #print out bye message from server
    #print(data.decode())

    

client.close()
