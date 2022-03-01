import sys

import socket


def conectTo():

    serverhost = sys.argv[1]
    serverportNumber = int(sys.argv[2])
    requiredFile = sys.argv[3]
    
    sizeofBuffer = 4096

    filecontent = open(requiredFile,'rb')
    filedata = filecontent.readlines()

    message = ''
    for each in filedata:
        message += each.decode('utf-8')

    tcpsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    tcpsock.connect((serverhost,serverportNumber))
    
    tcpsock.send(each.encode('utf-8'))
    resultantdata = tcpsock.recv(sizeofBuffer)
    tcpsock.close()

    print("Received data in the form of ",resultantdata)

conectTo()