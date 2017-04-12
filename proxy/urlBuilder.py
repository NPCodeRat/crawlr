import urllib2
from postcodes import PostCoder
from model.emp import Emp
from model.pay import Pay
from model.posted import Posted
from model.radius import Radius

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


class UrlBuilder:
    """Build URL list for CareerBuilder searches"""
    def __init__(self, search, zip):
        self._search = search
        self._zip = zip
        self.emp = Emp.cmd_append()
        self.pay = Pay.cmd_append()

    @property
    def search(self):
        return self._search

    @search.setter
    def search(self, s):
        self._search = s

    @property
    def zip(self):
        return self._zip

    @zip.setter
    def zip(self, z):
        pc = PostCoder()
        self._zip = z
        if not pc.get(z):
            print 'Invalid zip code. Defaulting to 21201'
            self._zip = '21201'
        else:
            self._zip = z
