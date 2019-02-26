from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup



def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None


title = getTitle("http://www.pythonscraping.com/pages/page1.htmlhttp://www.pythonscraping.com/pages/page1.html")


print(title)	
# try:
# 	html = urlopen("http://www.pythonscraping.com/pages/page1.htmlhttp://www.pythonscraping.com/pages/page1.html")
# except HTTPError as e:
# 	print(e)
# except URLError as e:
# 	print("The Server could not be found!")
# else:
# 	print("Its Worked")


