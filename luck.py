#!/usr/local/bin/python3
# luck.py - Open several Google search results.

import requests
import sys
import webbrowser
import bs4

print('Googling...')

# https://www.baidu.com/s?wd=jjj

google_base_url = 'http://www.baidu.com/s?wd='
res = requests.get(google_base_url + ' '.join(sys.argv[1:]))
res.raise_for_status()

# TODO: Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "html.parser")

# TODO: Open a browser tab for each result.
linkElems = soup.select('.t a')
print(len(linkElems))
numOpen = min(5, len(linkElems))
print(numOpen)
for i in range(numOpen):
	print(linkElems[i])
	webbrowser.open(linkElems[i].get('href'))
