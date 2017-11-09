from random import choice, randrange
from string import ascii_lowercase as lc
import re


def create_dm():
    name = ''.join(choice(lc) for j in range(randrange(1, 8)))
    subdomain = ''.join(choice(lc) for j in range(randrange(1, 15)))
    domain = choice(['ru', 'com', 'org'])
    return '{0}@{1}.{2}'.format(name, subdomain, domain)


f = open(r'/home/mj/redata.txt', 'r')
for line in f:
    print(re.subn(re.findall(r'::(.+)::', line)[0], create_dm(), line)[0].strip())
