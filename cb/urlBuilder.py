from pyzipcode import ZipCodeDatabase
from model.emp import Emp
from model.posted import Posted
from model.radius import Radius
from model.pay import Pay

# Default search settings:
#   "CareerBuilder Apply Only": "NO"
#   "Job Category": "Information Technology"
#   "Company": "All"
#   "Annual Pay": "Any"
#   "Employment Type": "All"
#   "Distance": "5 miles"
#   "Date Posted": "30 days"
#   "Query string": "None"
#   "Zipcode": "21201"


class UrlBuilder(object):
    zcdb = ZipCodeDatabase()
    """Build URL list for CareerBuilder searches"""
    def __init__(self, zipcode, search=None):
        self.search = search
        try:
            self.zcdb[zipcode]
        except IndexError:
            print 'Invalid zipcode code. Defaulting to 21201'
            self.zipcode = '21201'
        else:
            self.zipcode = zipcode
        self.base = 'http://www.careerbuilder.com/'
        self.params = []
        self.params.append(Posted.cmd_append())
        self.params.append(Radius.cmd_append())
        self.params.append(Pay.cmd_append())
        self.params.append(Emp.get_formatted())

    def build_url(self):
        if not self.has_filters():
            return self.base + self.build_path()
        else:
            return self.base + self.build_path() + self.format_filters()

    def build_path(self):
        if not self.search or not self.search.split():
            return 'jobs-in-{}'.format(self.zipcode)
        else:
            return 'jobs-{}-in-{}'.format('-'.join(self.search.split()), self.zipcode)

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
