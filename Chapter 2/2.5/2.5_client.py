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
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = input('>')
        s.sendall(bytes(data, 'utf-8'))
        while True:
            data = s.recv(1024)
            if not data.decode('utf-8') == '\n':
                # d = 1 / 0
                break
            print('Received', repr(data))  # Echo client program
    s.close()


cli()
