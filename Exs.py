from Exscript import Account
from Exscript.protocols import ssh2
import re,time

acc = Account('sbt-bedarev-ev', 'Qq123456!')

mac = '4fc9'

conn = ssh2.SSH2()
conn.connect('172.29.110.22')
conn.login(acc)
conn.execute('sys')
conn.execute('display mac-address | inc ' + mac)

data = conn.response

fnd_mac = re.findall(r'(?im)^[a-z0-9]{4}-[a-z0-9]{4}-' + mac + '.+GE(\d/0/\d{1,2})', data)

if len(fnd_mac) > 0:
    print(fnd_mac)
else:
    print('nothing find')

time.sleep(5)
conn.execute('quit')
conn.close()



