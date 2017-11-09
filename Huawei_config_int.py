import re
data = 'interface range gW/0/1 to gW/0/48'
for i in range(0, 5):
    dat = re.subn(r'W', str(i), data)
    print(dat[0])
    # f = open(r'/home/mj/rr1.txt', 'r')
    # for line in f:
    #     print(line.strip())
    # f.close()
    print('undo shutdown')
    print('quit')