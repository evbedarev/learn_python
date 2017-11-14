import paramiko

host = '172.29.110.21'
user = 'sbt-bedarev-ev'
secret = 'Qq123456!'
port = 22

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=secret, port=port)
stdin, stdout, stderr = client.exec_command('sys')
data = stdout.read() + stderr.read()

for line in data.decode('ascii').split('\n'):
    print(line)

client.connect(hostname=host, username=user, password=secret, port=port)
stdin, stdout, stderr = client.exec_command('interface g1/0/1')
data = stdout.read() + stderr.read()

# stdin, stdout, stderr = client.exec_command('di th')
# data = stdout.read() + stderr.read()

# for line in data.decode('ascii').split('\n'):
#     print(line)
client.close()


# import paramiko
# import time
#
# client = paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect('172.29.110.21', 22, 'sbt-bedarev-ev', 'Qq123456!')
#
# channel = client.get_transport().open_session()
# channel.get_pty()
# channel.settimeout(10)
# channel.exec_command('cd /share')
# print(channel.recv(1024))
# time.sleep(2)
# channel.exec_command('ls -l')
# print(channel.recv(1024))
# channel.close()
# client.close()