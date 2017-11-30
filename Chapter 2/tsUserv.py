from socket import *
from time import ctime

HOST = '172.29.98.0'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('waiting for connection...')
    data, addr = udpSerSock.recvfrom(BUFSIZE)
    udpSerSock.sendto(bytes('[' + str(ctime()) + ']' + data.decode('utf-8'), 'utf-8'), addr)
    print('...received from and returned to: ', addr)

udpSerSock.close()