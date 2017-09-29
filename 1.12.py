import re
data = '''https://www.google.ru/search?q=teamviewer&oq=team&aqs=chrome.1.69i57j0j69i61j0l3.2079j0j7&sourceid=chrome&ie=UTF-8'''
print(re.match(r'(https?://([A-Za-z0-9._?=&]/?)+(?:\.html)?)', data).group(0))