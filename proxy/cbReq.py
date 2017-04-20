import urllib2

from bs4 import BeautifulSoup

from urlBuilder import UrlBuilder


class CBReq(object):
    """Execute requests to CareerBuilder"""
    # zipcode = raw_input('Let\s scrape!  Query CareerBuilder.com for what zipcode?\n')
    # search = raw_input('\nEnter any job description keywords to search separated by spaces:\n')
    # x = UrlBuilder(zipcode, search)
    # page = urllib2.urlopen(x.build_url())
    # soup = BeautifulSoup(page, 'html.parser')
    # print soup

    @staticmethod
    def start():
        zipcode = raw_input('Let\s scrape!  Query CareerBuilder.com for what zipcode?\n')
        search = raw_input('\nEnter any job description keywords to search separated by spaces:\n')
        x = UrlBuilder(zipcode, search)
        print 'Querying CareerBuilder.com...'
        page = urllib2.urlopen(x.build_url())
        soup = BeautifulSoup(page, 'html.parser')
        print 'Query complete'
        return soup
