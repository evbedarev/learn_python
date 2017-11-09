import re
# data = 'clear configuration interface g4/0/W'
data = 'interface g1/0/W'
for i in range(1, 49):
    dat = re.subn(r'W', str(i), data)
    print(dat[0])
    # print('y')
    print('undo shutdown')