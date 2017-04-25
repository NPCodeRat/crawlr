class Distance(object):
    """Pull distance from zipcode parameter from a CB search"""

    @classmethod
    def pull_distance(cls, soup):
        distances = []
        parents = soup.findAll('div', 'columns end large-2 medium-3 small-12')
        for parent in parents:
            # TODO Wrap all in try catch
            distances.append(parent.find('h4', 'job-distance').contents[0].strip())
        return distances
