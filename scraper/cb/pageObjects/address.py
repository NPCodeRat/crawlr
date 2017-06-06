class Address(object):
    """Pull city / neighborhood and state from a CB search"""

    @classmethod
    def pull_addresses(cls, soup):
        """Find all address data in provided soup"""
        addresses = []
        parents = soup.findAll('div', 'columns end large-2 medium-3 small-12')
        for parent in parents:
            try:
                addresses.append(parent.find('h4', 'job-text').contents[0].strip())
            except AttributeError:
                addresses.append(None)
        return addresses
