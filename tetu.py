# -*- coding: utf-8 -*-

import urllib.request
import bs4

url = 'https://transit.yahoo.co.jp/traininfo/detail/77/0/'
html = urllib.request.urlopen(url).read()
soup = bs4.BeautifulSoup(html, 'lxml')



informationElement = soup.find('div', {'id': 'mdServiceStatus'})
information = informationElement.find('p').find(text=True, recursive=False)

postingDateElement = informationElement.find('p').find('span')
postingDate = ''
if postingDateElement is not None:
    postingDate = postingDateElement.find(text=True, recursive=False)

print(information + postingDate)
