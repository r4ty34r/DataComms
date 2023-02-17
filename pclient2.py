# Oscar Bruno
# Lab 1 part 2
# Client code 

import socket


# Initializing socket object configured to IP and TCP 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding the socket to IP and port
client.connect(('localhost',7500))  

# Data structure to hold message
messageList = []

# Program control variable
x = 0

while x == 0:
    message1 = "Hello Fordham"
    if len(message1) == 0 :continue
    
    # send data
    client.send(message1.encode())  
    print("Message 1 sent")
    
    # receive data
    data = client.recv(1024)
    
    # Storing message in list 
    messageList.append(data.decode())

    # Printing received message to console
    print("Returned from server:", data.decode())

    
    message2 = "Hello CISC 4615"
    client.send(message2.encode())
    print("Message 2 sent")

    response2 = client.recv(1024)
    messageList.append(response2.decode())
    print("Returned from server:", response2.decode())
    x+=1

    if data.decode() == 'Bye':
        x=1
        break

 
client.close()
print("\nSocket closed")

print("\nMessage history:")
for i in messageList:
    print(i)

print("\nProgram terminated")