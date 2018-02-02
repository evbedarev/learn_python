from socket import *
import time


HOST = '127.0.0.1'
PORT = getservbyname('daytime')
BUFSIZE = 1024
ADDR = (HOST, PORT)


cli = socket(AF_INET, SOCK_DGRAM)
cli.connect(ADDR)
cli.sendall(bytes('1'))
data = cli.recv(1024)
print(data.decode('utf-8'))