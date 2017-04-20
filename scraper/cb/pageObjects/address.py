class Address(object):
    """Pull city / neighborhood and state from a CB search"""

    @classmethod
    def pull_addresses(cls, soup):
        addresses = []
        parents = soup.findAll('div', 'columns end large-2 medium-3 small-12')
        for parent in parents:
            addresses.append(parent.find('h4', 'job-text').contents[0].strip())
        return addresses
