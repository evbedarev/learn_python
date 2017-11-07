import re
data = 'clear configuration interface gW/0/48'
for i in range(1, 5):
    dat = re.subn(r'W', str(i), data)
    print(dat[0])
    print('y')