from scraper.processing.aggregateData import AggregateData
from urlBuilder import UrlBuilder

from scraper.cb.paginationHandler import PaginationHandler


class CBReq(object):
    """Execute requests to CareerBuilder"""

    @classmethod
    def start(cls):
        zipcode = raw_input('Let\s scrape!  Query CareerBuilder.com for what zipcode?\n')
        search = raw_input('\nEnter any job description keywords to search separated by spaces:\n')
        x = UrlBuilder(zipcode, search)
        # BEGIN EXTRACT TO SCRAPEHANDLER
        # ex: scrapehandler.pullData(x.build_url())
        soups = PaginationHandler.paginate(x.build_url())
        AggregateData.pull_all(soups)
        # print 'Querying CareerBuilder.com...'
        # page = urllib2.urlopen(x.build_url())
        # soup = BeautifulSoup(page, 'html.parser')
        # print 'Query complete'
        # END EXTRACT
        # return soup
