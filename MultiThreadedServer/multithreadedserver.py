import socket


def connectionfromServer():

    serverhost = '192.168.0.241'
    serverportNumber = 6789
    sizeofBuffer = 4096
    
    tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpSock.bind((serverhost,serverportNumber))
    tcpSock.listen(1)

    connection,address = tcpSock.accept()

    print("Connection is established",address)
 
    while 1:
       
        message = connection.recv(sizeofBuffer)
        if not message:
            break
            
        print("Received message in the form of",message)
        connection.send(message)

    connection.close()

connectionfromServer()