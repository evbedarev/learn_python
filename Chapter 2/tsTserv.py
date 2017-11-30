from socket import *
from time import ctime, sleep
HOST = '172.29.98.0'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
try:
    while True:
        print('waiting for connection...')
        tcpCliSock, addr = tcpSerSock.accept()
        print('...connected from:', addr)
        while True:
            data = tcpCliSock.recv(BUFSIZE)
            if not data:
                break
            print(data)
            tcpCliSock.send(bytes('[' + str(ctime()) + ']' + ' ' + data.decode('utf-8'), 'utf-8'))

        tcpCliSock.close()

except KeyboardInterrupt:
    tcpSerSock.close()

finally:
    tcpSerSock.close()
