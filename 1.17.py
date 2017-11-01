import re
f = open(r'/home/mj/redata.txt', 'r')
wk = {'Mon': 0, 'Tue': 0, 'Wed': 0, 'Thu': 0, 'Fri': 0, 'Sat': 0, 'Sun': 0}
mon = {'Jan': 0, 'Feb': 0, 'Mar': 0, 'Apr': 0, 'Jun': 0, 'Jul': 0, 'Aug': 0, 'Sep': 0, 'Oct': 0, 'Nov': 0, 'Dec': 0, }
for i in re.finditer('(?im)^(\w{3}) (\w{3})', f.read()):
    wk.update({i.group(1): wk.get(i.group(1)) + 1})
    mon.update({i.group(2): mon.get(i.group(2)) + 1})
print(wk)
print(mon)
