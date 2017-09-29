import re
data = '''12312311'''
print(re.search(r'(\d+(.\d+e?-?(\d+)?))', data).group(0))