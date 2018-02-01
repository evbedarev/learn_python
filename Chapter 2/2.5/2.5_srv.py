from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSrvSock = socket(AF_INET, SOCK_STREAM)
tcpSrvSock.bind(ADDR)
tcpSrvSock.listen(5)

# try:
while True:
    print('waiting for connection')
    tcpCliSock, addr = tcpSrvSock.accept()
    print('connected from: ', addr)
    while True:
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        tcpCliSock.send(bytes('[{0}] {1}'.format(str(ctime()), data.decode('utf-8')), 'utf-8'))
        tcpCliSock.close()


# except Exception as e:
#     print(e)
#
# finally:
tcpSrvSock.close()