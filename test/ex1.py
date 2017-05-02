from scraper.processing.csvUtil import CSVUtil
from urlBuilder import UrlBuilder
from proxy.cbReq import CBReq
import os.path
import csv
from scraper.cb.pageObjects.postTime import PostTime


# if os.path.exists('../data/test.csv'):
#     os.remove('../data/test.csv')
# data = open('../data/test.csv', 'w')
# write = csv.writer(data, quoting=csv.QUOTE_ALL)
# write.writerow()

x = CBReq.start()
# print SelfRef.get()
CSVUtil.build(x)

# x = UrlBuilder('55555', 'test')
# print x.build_url()
# print x.zipcode
# print x.search
# print x.params
# x.build_url()

# Posted.cmd_append()

# urlStr = "http://www.careerbuilder.com/jobs-in-21212?cat1=JN008&page_number=1&radius=5"
# print "Querying: " + urlStr
# page = urllib2.urlopen(urlStr)
# soup = BeautifulSoup(page)
# titles = []
# for listings in soup.findAll('h2', attrs={'class': 'job-title'}):
#     for title in listings.findAll('a'):
#         titles.append(title.getText())
# print titles
