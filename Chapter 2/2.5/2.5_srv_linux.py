from socket import *
import time
from time import ctime
import os

HOST = '127.0.0.1'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSrvSock = socket(AF_INET, SOCK_STREAM)
tcpSrvSock.bind(ADDR)
tcpSrvSock.listen(5)

try:
    while True:
        print('waiting for connection')
        tcpCliSock, addr = tcpSrvSock.accept()
        print('connected from: ', addr)
        while True:
            data = tcpCliSock.recv(BUFSIZE)
            if not data:
                break
            print(data.decode('utf-8'))
            if data.decode('utf-8') == 'date':
                tcpCliSock.send(bytes(str(ctime())))
            elif data.decode('utf-8') == 'os':
                tcpCliSock.send(bytes(os.name))
            elif data.decode('utf-8') == 'ls':
                for i in os.listdir(os.curdir):
                    tcpCliSock.send(bytes(i + '\n'))
                    time.sleep(1)
                tcpCliSock.send(bytes('\n'))
            else:
                tcpCliSock.send(bytes('[{0}] {1}'.format(str(ctime()), data.decode('utf-8'))))



except Exception as e:
    print(e)
#
finally:
    tcpSrvSock.close()