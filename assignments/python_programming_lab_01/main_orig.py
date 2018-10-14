# import socket module
from socket import *

HOST = ""
PORT = 8080
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((HOST, PORT))
serverSocket.listen(1)

while True:
    # enstablish the connection
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()
    print("Client: ", addr[0])
    try:
        message = connectionSocket.recv(1024)
        print(message)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.readlines()
        f.close()
        # send one http header line to socket
        response = "HTTP/1.1 200 OK\r\n\r\n"
        print(response)
        connectionSocket.send(response.encode("utf-8"))
        # send the content of the request file to client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode("utf-8"))
            print(outputdata[i])
    except IOError:
        # Send response message for file not found
        notfound = "HTTP/1.1 404 Not Found\r\n\r\n"
        connectionSocket.send(notfound.encode("utf-8"))
        print(notfound)
    # Close client socket
    finally:
        connectionSocket.close()
serverSocket.close()
