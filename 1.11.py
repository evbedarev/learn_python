import re
data = '''SBT-Brerwrw-QWE@sberbank.ca.sbrf.ru'''
print(re.match(r'([A-Za-z0-9-]+@(?:[a-z]+.)+(?:ru|com|org))', data).group(0))