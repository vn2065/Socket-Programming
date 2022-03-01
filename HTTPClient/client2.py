import sys
import socket
serverHost = sys.argv[1]
serverPort = int(sys.argv[2])
filename = sys.argv[3]
buffer_size = 4096

message = ''
with open(filename, 'rb') as f:
	for msg in f:
		message += msg.decode('utf-8')

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.connect((serverHost,serverPort))

serverSocket.send(message.encode('utf-8'))


while(True):
    message= serverSocket.recv(buffer_size)
    if message:
        print("The message received is:", message)
serverSocket.close()

