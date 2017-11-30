from socket import *
HOST = '172.29.98.0'
PORT = 21566
BUFSIZE = 1024
ADDR = (HOST, PORT)
tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('>')
    if not data:
        break
    tcpCliSock.send(bytes(data, 'utf-8'))
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        print('failed')
        break
    print(data.decode('utf-8'))
tcpCliSock.close()