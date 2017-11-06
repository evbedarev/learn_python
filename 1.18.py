import re
f = open(r'C:\TEMP\redata.txt', 'r')
for line in f:
    print(re.findall(r' (\d+:\d+:\d+) ', line)[0])