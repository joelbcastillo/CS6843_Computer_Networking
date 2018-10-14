# Import socket module
from os import environ
from socket import *
import sys # In order to terminate the program

# Constants
HOST = environ.get('HOST', '127.0.0.1')
PORT = environ.get('PORT', 8080)
DEBUG = environ.get('DEBUG', True) # Change this to False to disable debug output
HTTP_OK = 'HTTP/1.1 200 OK\r\n\r\n'
HTTP_NOT_FOUND = 'HTTP/1.1 404 Not Found\r\n\r\n'

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
serverSocket.bind((HOST, PORT))
serverSocket.listen(1)

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    if DEBUG:
        print('Client: {}'.format(addr[0]))
    try:
        message = connectionSocket.recv(1024)
        if DEBUG:
            print('Message: {}'.format(message))
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.readlines()
        if DEBUG:
            print("OutputData: {outputdata}".format(outputdata=outputdata))
        
        # Send one HTTP header line into socket
        connectionSocket.send(HTTP_OK.encode())
        
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

    except IOError:
        # Send response message for file not found
        connectionSocket.send(HTTP_NOT_FOUND.encode())

    finally:        
        # Close client socket
        connectionSocket.close()
    
    serverSocket.close()
    # Terminate the program after sending the corresponding data
    sys.exit() 