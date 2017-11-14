import re

g = open(r'/home/mj/file.html', 'w')
g.writelines(['<html>\n', ' <head><title>Examples of links</title></head>\n',
              '  <body>\n',
              ])
f = open(r'/home/mj/html.txt', 'r')
for line in f:
    links = re.findall(r'([A-Za-z:/\.-]+)(?:, )?([A-Za-z:/\. ]+)?', line)[0]
    print(links[0])
    if links[1] != '':
        g.writelines('    <p><a href="' + links[0] + '">' + links[1] + '</a></p>\n')
    else:
        g.writelines('    <p><a href="' + links[0] + '">' + links[0] + '</a></p>\n')
g.writelines('</body>')

g.close()
f.close()