from proxy.urlBuilder import UrlBuilder
from model.posted import Posted

# x = UrlBuilder(21212, 'search')
# print x.zip
# print x.search
# print x.emp
# print x.pay

Posted.cmd_append()

# urlStr = "http://www.careerbuilder.com/jobs-in-21212?cat1=JN008&page_number=1&radius=5"
# print "Querying: " + urlStr
# page = urllib2.urlopen(urlStr)
# soup = BeautifulSoup(page)
# titles = []
# for listings in soup.findAll('h2', attrs={'class': 'job-title'}):
#     for title in listings.findAll('a'):
#         titles.append(title.getText())
# print titles
