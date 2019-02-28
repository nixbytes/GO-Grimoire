from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup



def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read())
		title = bsObj.body.h1
	except AttributeError as e:
		return None
		
	return None


title = getTitle("http://www.pythonscraping.com/pages/page1.html")

if title == None:
	print("Title could not be found")
else:
	print(title)



### Dealing with children and other descendants

html = urlopen("http://www.pythonscraping.com/pages/page3.html")

bsObj = BeautifulSoup(html)

for child in bsObj.find("table",{"id":"giftList"}).children:
	print(child)



