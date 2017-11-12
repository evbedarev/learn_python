# import paramiko
#
# host = '192.168.1.51'
# user = 'admin'
# secret = 'Qq123456'
# port = 22
#
# client = paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect(hostname=host, username=user, password=secret, port=port)
# stdin, stdout, stderr = client.exec_command('ls -l')
# data = stdout.read() + stderr.read()
#
# for line in data.decode('ascii').split('\n'):
#     print(line)
#
# stdin.write('cd /share' + '\n')
# stdin.flush()
#
# stdin, stdout, stderr = client.exec_command('ls -l')
# data = stdout.read() + stderr.read()
#
# for line in data.decode('ascii').split('\n'):
#     print(line)
# client.close()


import paramiko
import time

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.1.51', 22, 'admin', 'Qq123456')

channel = client.get_transport().open_session()
channel.get_pty()
channel.settimeout(10)
channel.exec_command('cd /share')
print(channel.recv(1024))
time.sleep(2)
channel.exec_command('ls -l')
print(channel.recv(1024))
channel.close()
client.close()