from pyzipcode import ZipCodeDatabase
from model.rad import Rad

# Default search settings:
#   "Job Category": "Software Engineer"
#   "Employment Type": "All"
#   "Distance": "5 miles"
#   "Query string": "None"
#   "Zipcode": "21201"


class UrlBuilder(object):
    zcdb = ZipCodeDatabase()
    """Build URL list for Monster searches"""
    def __init__(self, zipcode):
        self.base = 'https://www.monster.com/jobs/search/'
        self.params = []
        try:
            self.zcdb[zipcode]
        except IndexError:
            print 'Invalid zipcode code. Defaulting to 21201'
            self.params.append('where=21201')
        else:
            self.params.append('where={}'.format(zipcode))
        self.params.append(Rad.cmd_append())

    def build_url(self):
        if not self.has_filters():
            return '{}/Software-Engineer_5'.format(self.base)
        else:
            return '{}/Software-Engineer_5{}'.format(self.base, self.format_filters())

    def has_filters(self):
        if any(param is not None for param in self.params):
            return True
        else:
            return False

    def format_filters(self):
        base = '?'
        for param in self.params:
            if param is not None:
                base += param + '&'
        return base.rstrip('&')
