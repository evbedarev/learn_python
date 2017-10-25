from random import randrange, choice
from string import ascii_lowercase as lc
import struct
from time import ctime

maxint = 2 ** (struct.Struct('i').size * 8 - 1) - 1
tlds = ('com', 'edu', 'net', 'org', 'gov')
f = open(r'/home/mj/redata.txt', 'w')

for i in range(randrange(5, 11)):
    dtint = randrange(maxint)
    dtstr = ctime(dtint)
    llen = randrange(4, 8)
    dlen = randrange(llen, 13)
    login = ''.join(choice(lc) for j in range(llen))
    dom = ''.join(choice(lc) for j in range(dlen))
    f.writelines('{0}::{1}@{2}.{3}::{4}-{5}-{6} \n'.format(dtstr, login, dom, choice(tlds), dtint, llen, dlen))
    # print('{0}::{1}@{2}.{3}::{4}-{5}-{6}'.format(dtstr, login, dom, choice(tlds), dtint, llen, dlen))
