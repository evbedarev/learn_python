import re
def book(http, region, out):
    lnk = 'http://amazon.XX/dp/0132678209'
    if region in ['de','fr','jp','cn','co.uk']:
        lnk = re.sub('XX', region, lnk)
    else:
        lnk = re.sub('XX', 'com', lnk)
    print(lnk)

def ttt():
    from lxml import html, etree
    import urllib.request as request
    from urllib import request
    from urllib.parse import urlparse
    response = request.urlopen('https://www.amazon.com/dp/0132678209', timeout=40)
    page = html.parse(response)
    e = page.getroot().find_class('a-size-medium a-color-price header-price').pop()
    print(e.text.strip())

ttt()