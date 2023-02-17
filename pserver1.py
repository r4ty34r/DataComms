# Oscar Bruno
# Lab 1 part 1
# Server code 

#Initializing socket 
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

portnum = 7202
# Bind socket to ip 
server.bind(('localhost', portnum))

# Configure listen
server.listen(5)

print(f"Listening configured on port: {portnum}")

#List to store message history 

messageList = []

# Program control variable
x = 0

# Main program loop
while True:
    #program loop control 
    message2 = "Bye"

    # Accepting a connection
    (clientSocket,clientAddress) = server.accept()
    print("\nAccepted connection from", clientAddress)

    while x == 0:
        # Receiving data from socket
        data = clientSocket.recv(1024)
        print("Received data from client: ",data.decode())
        messageList.append(data.decode())

        #echo message back to client
        clientSocket.send(message2.encode())
        
        # Exiting data reading loop
        x +=1
    break

# Closing socket
server.close()
print ("\nSocket closed")

# Printing message history after closing connection
print("Message history from client: ")
for i in messageList:
    print(i)

