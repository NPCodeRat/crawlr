from monster.urlBuilder import UrlBuilder
from scraper.monster.paginationHandler import PaginationHandler
from scraper.processing.aggregateData import AggregateData


class MonsterReq(object):
    """Execute requests to Monster"""

    @classmethod
    def start(cls):
        zipcode = raw_input('\nScraping!  Query Monster.com for what zipcode?\n')
        x = UrlBuilder(zipcode)
        soups = PaginationHandler.paginate(x.build_url())
        return AggregateData.pull_monster(soups)
