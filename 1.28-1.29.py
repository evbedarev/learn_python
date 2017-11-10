import re
data = '(800)555-1212'
print(re.findall(r'(((\d{3}-)|(\(\d{3}\)))?\d{3}-\d{4})', data)[0][0])
