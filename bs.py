#http://www.crummy.com/software/BeautifulSoup/
from BeautifulSoup import BeautifulSoup
html = "<html><body><p>test</p></body></html>"
soup = BeautifulSoup(html)
print soup.findAll("p")[0].contents
dir(soup)
