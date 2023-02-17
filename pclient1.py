# Oscar Bruno
# Lab 1 part 1
# Client code 

import socket

# Initializing socket object configured to IP and TCP 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding the socket to IP and port
client.connect(('localhost',7202))  

# Data structure to hold message
messageList = []

# Program control variable
x = 0

while x == 0:

    #Read in the input
    message1 = input(">>:").strip()

    if len(message1) == 0 :continue
    
    # send data
    client.send(message1.encode())  
    
    # receive data
    data = client.recv(1024)

    # Storing message in list 
    messageList.append(data.decode())

    # Printing received message to console
    print("Returned from server:", data.decode())
    check = data.decode()

    if check == 'Bye':
        x=1
        break


client.close()
print("\nSocket closed")

print("\nMessage history from server:")
for i in messageList:
    print(i)

print("\nProgram terminated")