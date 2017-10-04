import re
data = "12"
print(re.match(r'1[0-2]', data).group(0))