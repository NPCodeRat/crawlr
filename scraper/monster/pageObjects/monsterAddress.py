class MonsterAddress(object):
    """Pull addresses from Monster search"""

    @classmethod
    def pull_addresses(cls, soup):
        addresses = []
        parents = soup.findAll('div', 'job-specs job-specs-location')
        for parent in parents:
            try:
                addresses.append(parent.find('a').contents[0].strip())
            except AttributeError:
                addresses.append(parent.find('a'))
        return addresses
