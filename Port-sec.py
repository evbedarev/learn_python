from Exscript import Account
from Exscript.protocols import ssh2
import re, time


class huawei():
    ip = ''
    user = ''
    password = ''
    mac = ''

    def __init__(self, ip, user, password, mac):
        self.ip = ip
        self.user = user
        self.password = password
        self.mac = mac

    def connect(self):
        acc = Account(self.user, self.password)
        conn = ssh2.SSH2()
        conn.connect(self.ip)
        time.sleep(3)
        conn.login(acc)
        return conn

    #Поиск мак адреса
    def exec_cmd(self):
        conn = self.connect()
        conn.execute('sys')
        conn.execute('display mac-address | inc ' + self.mac)
        data = conn.response
        fnd_mac = re.findall(r'(?im)^[a-z0-9]{4}-[a-z0-9]{4}-' + self.mac + '.+GE(\d/0/\d{1,2})', data)
        try:
            conn.close(True)
        except Exception:
            print('error while close ssh connection')

        if len(fnd_mac) > 0:
            return(fnd_mac)
        else:
            return('On switch ' + self.ip + ' nothing find')

    ###ОЧиска порта
    def clear_port(self, interface):
        conn = self.connect()
        conn.execute('sys')
        for i in interface:
            conn.execute('interface ' + i)
            conn.execute('undo port-security mac-address sticky')
            time.sleep(1)
            conn.execute('port-security mac-address sticky')
            time.sleep(1)
            conn.execute('restart')
        try:
            conn.close(True)

        except Exception:
            print('error while close ssh connection')


class Cisco(huawei):
    def exec_cmd(self):
        conn = self.connect()
        conn.execute('show mac address-table | inc ' + self.mac)
        data = conn.response
        fnd_mac = re.findall(r'(?im).+[a-z0-9]{4}\.[a-z0-9]{4}\.' + self.mac + '.+Gi(\d/0/\d{1,2})', data)
        try:
            conn.close(True)
        except Exception:
            print('error while close ssh connection')

        if len(fnd_mac) > 0:
            return(fnd_mac)
        else:
            return('On switch ' + self.ip + ' nothing find')

    def clear_port(self, interface):
        conn = self.connect()
        for i in interface:
            conn.execute('clear port-security all interface ' + i)
            time.sleep(1)
            conn.execute('conf t')
            time.sleep(0.5)
            conn.execute('interface ' + i)
            time.sleep(0.5)
            conn.execute('shu')
            time.sleep(0.5)
            conn.execute('no shu')
            time.sleep(0.5)
            conn.execute('exit')
            time.sleep(0.5)
            conn.execute('exit')
        try:
            conn.close(True)

        except Exception:
            print('error while close ssh connection')


###Cerd####
mac = '1fea'
user = 'sbt-bedarev-ev'
passwd = 'Qq123456!'
############################
# find = Cisco('172.29.110.5', user, passwd, mac)
# print(find.exec_cmd())
ip = ['172.29.110.5', '172.29.110.6']

def ZD(ip):
    for i in ip:
        find = Cisco(i, user, passwd, mac)
        respons = find.exec_cmd()
        if 'nothing find' in respons:
            pass
        else:
            print('On switch ' + i)
            print(respons)
            break
ZD(ip)

# find = huawei('172.29.110.22', user, passwd, mac)
# respons = find.exec_cmd()
# print('On switch 172.29.110.22:')
# print(respons)
# if 'nothing find' in respons:
#     find = huawei('172.29.110.21', user, passwd, mac)
#     respons = find.exec_cmd()
#     print('On switch 172.29.110.21:')
#     print(respons)
#     if 'nothing find' in respons:
#         find = huawei('172.29.110.15', user, passwd, mac)
#         respons = find.exec_cmd()
#         print('On switch 172.29.110.15:')
#         print(respons)