from BeautifulSoup import BeautifulSoup


class JobTitle(object):
    """Pull job titles from CB search"""
    titleFinder = ''

    @staticmethod
    def pull_titles(soup):
