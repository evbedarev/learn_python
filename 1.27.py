import re
f = open(r'/home/mj/redata.txt', 'r')
for line in f:
   print(re.subn(r'(\w{3}) (\w{3}) (\d+) (.+) (\d+)', r'\1 \2 , \3, \5, \4', line))
