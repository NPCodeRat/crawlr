import urllib2
from bs4 import BeautifulSoup


class PaginationHandler(object):
    """Manages all pagination requests for CB"""

    @classmethod
    def paginate(cls, url):
        soups = []
        print 'Querying CareerBuilder...'
        try:
            first_page = urllib2.urlopen(url)
        except urllib2.HTTPError:
            print 'No results.  Try again with fewer search parameters.'
        else:
            soups.append(BeautifulSoup(first_page, 'html.parser'))
            cls.subsequent_pages(url, soups)
        print 'Query complete'
        return soups

    @staticmethod
    def subsequent_pages(url, soups):
        print 'Checking for further pages of results...'
        counter = 2
        has_next = True
        # TODO remove count limiter!
        while has_next is True:
            try:
                next_page = urllib2.urlopen('{}&page_number={}'.format(url, counter))
            except urllib2.HTTPError:
                has_next = False
            else:
                print 'Querying result page {}'.format(counter)
                next_soup = BeautifulSoup(next_page, 'html.parser')
                counter += 1
                soups.append(next_soup)
        return soups
