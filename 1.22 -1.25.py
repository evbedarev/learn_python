import re
f = open(r'/home/mj/redata.txt', 'r')
for line in f:
    #1.22
    print(re.findall(r'(\d+)::', line)[0])
    #1.23
    print(re.findall(r'(\d+:\d+:\d+)', line)[0])
    #1.24
    fnd = re.findall(r'(::(\w+)@(.+)::)', line)
    print(fnd[0][1] + ' ' + fnd[0][2])
    # 1.25
    fnd = re.findall(r'(::(\w+)@(\w+)\.(\w+)::)', line)
    print(fnd[0][1] + ' ' + fnd[0][2] + ' ' + fnd[0][3])