class MonsterCompany(object):
    """Pull company names from Monster search"""

    @classmethod
    def pull_companies(cls, soup):
        """Find all company name data in provided soup"""
        companies = []
        parents = soup.findAll('div', 'company')
        for parent in parents:
            try:
                companies.append(parent.find('span').contents[0].strip())
            except AttributeError:
                companies.append(parent.find('span'))
        return companies
