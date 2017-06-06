import urllib2
from bs4 import BeautifulSoup


class PaginationHandler(object):
    """Manages all pagination requests for Monster"""

    @classmethod
    def paginate(cls, url):
        """Execute initial request and pull first soup, pass to subsequent_pages for pagination"""
        soups = []
        print 'Querying Monster...'
        try:
            first_page = urllib2.urlopen(url)
        except urllib2.HTTPError:
            print 'No results.  Try again with a different zipcode.'
        else:
            soups.append(BeautifulSoup(first_page, 'html.parser'))
            cls.subsequent_pages(url, soups)
        print 'Query complete'
        return soups

    @staticmethod
    def subsequent_pages(url, soups):
        """Determine whether request has subsequent pages of results, execute requests until pagination is exhausted"""
        print 'Checking for further pages of results...'
        counter = 2
        has_next = True
        while has_next is True:
            try:
                next_page = urllib2.urlopen('{}&page={}'.format(url, counter))
            except urllib2.HTTPError:
                has_next = False
            else:
                print 'Querying result page {}'.format(counter)
                next_soup = BeautifulSoup(next_page, 'html.parser')
                counter += 1
                soups.append(next_soup)
        return soups
