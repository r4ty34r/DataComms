//built for windows, OB
#include <iostream>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <Windows.h>
#define DEFAULT_PORT 52000
#define BUFFSIZE 1024

using namespace std;


int main(){
    //Initialize winsock2 object
    WSADATA wsData; //WSA = winsock api 

    //specifying version
    WORD ver = MAKEWORD(2,1);
    
    //
    int wsOk = WSAStartup(ver, &wsData);

    //If build setup above fails, log error and exit program
    if (wsOk != 0)
    {
        cerr << "\nFailed startup :(" << endl;
        return -1;
    }
    else
    {
        cout << "Winsock dll found" << endl;
        cout << "\nThe status: " << wsData.szSystemStatus << endl;
    }

    //Create a socket 
    SOCKET listening = socket(AF_INET, SOCK_STREAM, 0);

    //handle error in case setup fails
    if (listening == INVALID_SOCKET)
    {
        cout << "\nCan't create listening socket :(" << endl << "Error: " << WSAGetLastError() << endl;
        WSACleanup();
        return -1;
    }
    else
    {
        cout << "\nSocket is listening now on port: " << DEFAULT_PORT << endl;
    }

    //Bind ip address to port & socket

    sockaddr_in hint;
    hint.sin_family = AF_INET;
    hint.sin_port = htons(DEFAULT_PORT);
    
    

    hint.sin_addr.S_un.S_addr = INADDR_ANY; //inet_pton can also be used here
    
    //bind function to link listening socket to the network, if function does not return 0, throw error
    if(bind(listening, (sockaddr*)&hint, sizeof(hint)) == SOCKET_ERROR)
    {
        cout << "\nBind failed: " << WSAGetLastError() << endl;
        closesocket(listening);
        WSACleanup();  
        return -1; 
    } 
    else
    {
        cout << "\nSocket bound to ip" << endl;
    }

    //Configure for connection
    if(listen(listening, SOMAXCONN) == SOCKET_ERROR)//number of maximum connections possible 
    {
        cout << "\nError listening: " << WSAGetLastError();
        WSACleanup();
        return -1;
    } 
    else
    {
        cout << "\nListening for connections...." << endl;
    }

    //holding space for client 
    sockaddr_in client; 
    client.sin_family = AF_INET;
    
    client.sin_port = htons(DEFAULT_PORT);
    int clientSize = sizeof(client);
    cout << "\nClient data struct created" << endl;
    

    //When a connection happens
    SOCKET clientSocket = accept(listening, (sockaddr*)&client, &clientSize);
    if (clientSocket == INVALID_SOCKET)
    {
        cerr << "\nClient connection failed :( " << endl << WSAGetLastError(); WSACleanup();
    }
    else
    {
        cout <<"\nClient connection accepted!" << endl;
    }
    


    char host[NI_MAXHOST]; //client's remote name 
    char service[NI_MAXHOST]; // Port the client is connected on

    ZeroMemory(host, NI_MAXHOST); //on mac/linux this command is memset(host,0,NI_MAXHOST)
    ZeroMemory(service, NI_MAXHOST); //on mac/linux this command is memset(service,0,NI_MAXHOST)
 
    //check to see if we can get host info, if not, rely on connection data 
    cout << "\nMoving to gethostbyname......." << endl;

    //int hostcheck = getnameinfo((sockaddr*)&client, sizeof(client), host, NI_MAXHOST, service, NI_MAXSERV, 0);
   
   //TODO: FIX CONNECTION ISSUES. PROBLEMS WITH GETTING HOSTINFO
   struct addrinfo *res = NULL;

    int hostinfo = gethostname(host, sizeof(host));
    if (hostinfo != 0)
    {
        cout << "\nhostinfo is not 0 :(" << endl;
        cout << "\nError getting host info: " << WSAGetLastError();
    }
    //TODO: FIX CONNECTION ISSUES
    if (hostinfo==0)
    {
        cout << "\nhostinfo is 0... something wrong with service." << endl;
        cout << host << " connected on port: " << service << endl; 
    }
    else 
    {
        inet_ntoa(client.sin_addr);
        cout << host << " connectec on port: " << ntohs(client.sin_port) << endl;
    }
    
    //Close listening socket
    closesocket(listening); //will be modified later for multiple rounds of listening 

    //While loop: accept and echo message back to client 
    char buf[BUFFSIZE];
    
    while (true)
    {

        ZeroMemory(buf, BUFFSIZE);

        //wait for client to send data then 
        int bytesReceived = recv(clientSocket, buf, BUFFSIZE, 0);

        if (bytesReceived == SOCKET_ERROR)
        {
            cerr <<"\n ERROR IN: recv(). Quitting." << endl << WSAGetLastError(); //program stops here 
            return -1;
        }
        if (bytesReceived == 0)
        {
            cout << "Client disconnected. " << endl;
            break;
        }
        
        //Echoing back to the client socket from the buf the bytesreceived + last character
        send(clientSocket, buf, bytesReceived + 1, 0);

        //close socket
        closesocket(clientSocket);

        //Cleanup the socket
        WSACleanup();
    }

    //Close socket 

    //Shutdown winsock
    return 0;

}