import urllib2

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

class UrlBuilder():
    """Build URL list for CareerBuilder searches"""
    def __init__(self, search, zip):
        self.search = search
        self.zip = zip
