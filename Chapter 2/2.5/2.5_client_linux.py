# Echo client program
import socket


def wrap_try(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)

        except Exception as e:
            print('exception')
            print(e)

    return inner


@wrap_try
def cli():
    HOST = '127.0.0.1'  # The remote host
    PORT = 21567  # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    data = raw_input('>')
    s.sendall(bytes(data))
    while True:
        data = s.recv(1024)
        if data.decode('utf-8') == '\n':
            break
        print('Received', data.decode('utf-8'))  # Echo client program
    s.close()


cli()
