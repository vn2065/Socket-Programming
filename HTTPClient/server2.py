from importlib.util import module_for_loader
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
serverHost = '192.168.0.241'
serverPort = 6789
buffer_size = 4096

serverSocket.bind((serverHost, serverPort))
serverSocket.listen(5)

conn,addr = serverSocket.accept()
message = ''

while 1:
	message += (conn.recv(buffer_size).decode()) + '\n'
	if not message:
		break
	print("The received message is:", message)
conn.send(message)
conn.close()