class Distance(object):
    """Pull distance from zipcode parameter from a CB search"""

    @classmethod
    def pull_distance(cls, soup):
        """Find all distance-from-search-radius data in provided soup"""
        distances = []
        parents = soup.findAll('div', 'columns end large-2 medium-3 small-12')
        for parent in parents:
            try:
                distances.append(parent.find('h4', 'job-distance').contents[0].strip())
            except AttributeError:
                distances.append(None)
        return distances
