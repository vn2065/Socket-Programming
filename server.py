#import socket module
from socket import *
import sys                     # In order to terminate the program

def webServer(port):            #a function called webServer is declared
    """
    #Create a TCP server socket
    #(AF_INET is used for IPv4  protocols)
    #(SOCK_STREAM is used for TCP)
    #Prepare a server socket and assign it to a variable called serverSocket
    """
    serverSocket = socket(AF_INET, SOCK_STREAM)         
    #Fill in start
    """host ip address is assigned to a variable called serverHost """
    serverHost = 'localhost'                    
    buffer_size = 4096
    serverSocket.bind((serverHost, port)) 
    """ binds the serverSocket to the specified socket address, 
    i.e. IP address and port number """ 
    serverSocket.listen(1)  
    """Puts the server into listen mode. Allows the server to listen to incoming
    connections. Listen to at most 1 connection at a time."""
    #Fill in end
     
    #Server should be up running and listening to the incoming connections
    """infinite while loop to handle client requests 
    as long as server is running."""
    while True:            
    #Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        
        #If an exception occurs during the execution of the try clause the rest 
        # of the clause is skipped. If the exception type matches the word after except, 
        # the except clause is executed
        try:
            
            
            message = connectionSocket.recv(buffer_size)  
            """Receives the request message from the client"""
            #print(message.decode())
            """
            Extract the path of the requested object from the message. 
            The path is the second part of HTTP header, identified by [1]
            """
            filename = message.split()[1]
            
            """ Because the extracted path of the HTTP request includes 
            a character '\', we read the path from the second character """
            f = open(filename[1:].decode())

            outputdata = f.readlines() 
            """ Read the file "f" and store the entire content of the 
            requested file in a temporary buffer """
            
            """
            Send the HTTP response header line to the connection socket. 
            Format: "HTTP/1.1 *code-for-successful-request*\r\n\r\n"
            """
            connectionSocket.send(b"HTTP/1.1 200 OK\r\nContent-Type:text/html\r\n\r\n")
            #connectionSocket.send("\r\n".encode())
            
            """ Then we iterate through the contents of the file inorder to 
            send the content of the requested file to the connection socket """
            for i in range(0, len(outputdata)):  
                connectionSocket.send(outputdata[i].encode())
                print(outputdata[i])
            
            connectionSocket.close()    
            """ Close the client connection socket """
            
        
        except IOError:
            """
            Send HTTP response message for the file not found
            Same format as above, but with code for "Not Found"
            """
            connectionSocket.send(b"HTTP/1.1 404 Not Found\r\n\r\n")
            connectionSocket.send(b"Content-Type: text/html\r\n\r\n")
            
            connectionSocket.send(b"<html><head></head><body><h1>404 Not Found </h1></body></html>\r\n\r\n")
            connectionSocket.close() 
            """ Close the client connection socket """
            
            pass
    serverSocket.close()
    sys.exit() 
    """ Terminate the program after sending the corresponding data """
if __name__ == "__main__":
    webServer(6789)


