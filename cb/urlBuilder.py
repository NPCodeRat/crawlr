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
    """Build URL list for CareerBuilder searches"""
    zcdb = ZipCodeDatabase()

    def __init__(self, zipcode, search=None):
        """Validate zipcode, prompt user for all query parameters"""
        self.search = search
        try:
            # Check zipcode DB for valid zip
            self.zcdb[zipcode]
        except IndexError:
            # Default to Baltimore Catalyte office zipcode
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
        """Add path and query parameters based on filters specified by user"""
        if not self.has_filters():
            return '{}{}?cat1=JN008'.format(self.base, self.build_path())
        else:
            return '{}{}{}&cat1=JN008'.format(self.base, self.build_path(), self.format_filters())

    def build_path(self):
        """Compose URL substring for endpoint path"""
        if not self.search or not self.search.split():
            return 'jobs-in-{}'.format(self.zipcode)
        else:
            return 'jobs-{}-in-{}'.format('-'.join(self.search.split()), self.zipcode)

    def has_filters(self):
        """Check for user input query parameters"""
        if any(param is not None for param in self.params):
            return True
        else:
            return False

    def format_filters(self):
        """Compose URL substring for all query parameters"""
        base = '?'
        for param in self.params:
            if param is not None:
                base += param + '&'
        return base
