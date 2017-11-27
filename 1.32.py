import re


def book(region, out):

    lnk = 'http://amazon.XX/dp/0132678209'
    if region in ['de', 'fr', 'jp', 'cn', 'co.uk']:
        lnk = re.sub('XX', region, lnk)
    else:
        lnk = re.sub('XX', 'com', lnk)
    text = ttt(lnk, 0)
    if out == 'text':
        print(text)
    else:
        f = open('c:\TEMP\out.html')
        f.writelines('<p>' + text + '</p>')


def ttt(lnk, i):

    from lxml import html
    from urllib import request
    import time

    # if i == 0: i = 1
    # if i == 5: return 'Can not connect to link ' + lnk
    response = ''
    while response == '':
        try:
            response = request.urlopen(lnk, timeout=5)
            print('go to link ' + lnk)

        except Exception:
            print('Service unavailble')
            time.sleep(2)


    page = html.parse(response)
    e = page.getroot().find_class('a-size-medium a-color-price header-price').pop()
    return e.text.strip()

book('com','text')