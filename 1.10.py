import re
data = '''123.123-1.5j'''
print(re.match(r'((-?\d+\.?\d+)?[\+-]?\d+\.?(\d+)?j)', data).group(0))