# Lab 1 - Server program
# Due date: 2-17-23
# Oscar Bruno

# Initializing socket 
import socket

#Server object configured to IP and TCP
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Bind socket to IP 
portnum = 9000
server.bind(('localhost', 9000))

# Configure listen
server.listen(5)

print("Waiting for client on port: ",portnum)

# initializing buffer size
buf = 1024
server.accept()
while True:
    #accept connection
    conn,addr = server.accept()
    print(conn,addr)
    print("\nClient connected")

    while True:
        #read data from connection
        data = conn.recv(buf)
        print("\nData received ")

        if not data: 
            print("\nLost client")
            break

        # return data
        conn.send(data)
        if (data == 'bye'):
            break

#close socket
server.close()