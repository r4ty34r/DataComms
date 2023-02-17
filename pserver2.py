# Oscar Bruno
# Lab 1 part 2
# Server code 

#Initializing socket 
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

portnum = 7500
# Bind socket to ip 
server.bind(('localhost', portnum))

# Configure listen
server.listen(5)

print(f"Listening configured on port: {portnum}")

#List to store message history 

messageList = []

# messages to echo back to client 
message2 = "Hello CISC Students"
message3 = "Bye"

# Main program loop
while True:
    #program loop control 
    x = 0
    (clientSocket,clientAddress) = server.accept()
    print("\nAccepted connection from", clientAddress)

    while True:
        # Receiving first message
        data = clientSocket.recv(1024)

        # Printing first message
        print("Received data from client: ",data.decode())

        # Appending first message to list
        messageList.append(data.decode())

        # Sending first response back to client
        clientSocket.send(message2.encode())

        # Receiving second message
        data2 = clientSocket.recv(1024)

        # Printing second message to console
        print("Received data from client: ",data2.decode())

        # Appending second message to list
        messageList.append(data2.decode())
        


        # If the decoded message is correct, send bye, break out and close socket
        if (data.decode() == 'Hello CISC 4615'):
            clientSocket.send(message3.encode())
            x+=1
            break

        if not data:
            print("\nLost client")
            break
        

    if x != 0:
        print("Exiting Program loop")
        break

server.close()
print ("\nSocket closed")

print("Message history from client: ")

for i in messageList:
    print(i)

