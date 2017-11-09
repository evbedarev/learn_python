import re
f = open(r'/home/mj/redata.txt', 'r')
for line in f:
    print(re.findall(r'::(\d+)-', line)[0])