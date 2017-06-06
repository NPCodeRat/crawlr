from pyzipcode import ZipCodeDatabase
from model.rad import Rad

# Default search settings:
#   "Job Category": "Software Engineer"
#   "Employment Type": "All"
#   "Distance": "5 miles"
#   "Query string": "None"
#   "Zipcode": "21201"


class UrlBuilder(object):
    """Build URL list for Monster searches"""
    zcdb = ZipCodeDatabase()

    def __init__(self, zipcode):
        """Validate zipcode, prompt user for query parameter input"""
        self.base = 'https://www.monster.com/jobs/search/'
        self.params = []
        try:
            # Check zipcode DB for valid zip
            self.zcdb[zipcode]
        except IndexError:
            # Default to Baltimore Catalyte office zipcode
            print 'Invalid zipcode code. Defaulting to 21201'
            self.params.append('where=21201')
        else:
            self.params.append('where={}'.format(zipcode))
        self.params.append(Rad.cmd_append())

    def build_url(self):
        """Add path and query parameters based on filters specified by user"""
        if not self.has_filters():
            return '{}/Software-Engineer_5'.format(self.base)
        else:
            return '{}/Software-Engineer_5{}'.format(self.base, self.format_filters())

    def has_filters(self):
        """Check for user input query parameters"""
        if any(param is not None for param in self.params):
            return True
        else:
            return False

    def format_filters(self):
        """Compose URL substring for query parameters"""
        base = '?'
        for param in self.params:
            if param is not None:
                base += param + '&'
        return base.rstrip('&')
