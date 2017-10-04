import re
data = "<type 'builtin_function_or_method'>"
print(re.match(r'(<type \'(.+)\'>)', data).group(2))