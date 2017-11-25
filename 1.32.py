import re
def book(region, out):
    lnk = 'http://amazon.XX/dp/0132678209'
    if region in ['de','fr','jp','cn','co.uk']:
        lnk = re.sub('XX', region, lnk)
    else:
        lnk = re.sub('XX', 'com', lnk)
    text = ttt(lnk)
    if out == 'text':
        print(text)
    else:
        f = open('c:\TEMP\out.html')
        f.writelines('<p>' + text + '</p>')

def ttt(lnk):
    from lxml import html
    import urllib.request as request
    from urllib import request
    from urllib.parse import urlparse
    response = request.urlopen(lnk, timeout=40)
    page = html.parse(response)
    e = page.getroot().find_class('a-size-medium a-color-price header-price').pop()
    print(e.text.strip())
    return e.text.strip()
