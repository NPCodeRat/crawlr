from scraper.processing.aggregateData import AggregateData
from scraper.cb.paginationHandler import PaginationHandler
from cb.urlBuilder import UrlBuilder


class CBReq(object):
    """Execute requests to CareerBuilder"""

    @classmethod
    def start(cls):
        """Prompt user for input, build URL, execute paginated requests, and pass to AggregateData"""
        zipcode = raw_input('Scraping!  Query CareerBuilder.com for what zipcode?\n')
        search = raw_input('\nEnter any job description keywords to search separated by spaces:\n')
        x = UrlBuilder(zipcode, search)
        soups = PaginationHandler.paginate(x.build_url())
        return AggregateData.pull_all(soups)
