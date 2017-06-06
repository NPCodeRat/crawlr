class Company(object):
    """Pull hiring company name from CB search"""

    @classmethod
    def pull_companies(cls, soup):
        """Find all company name data in provided soup"""
        companies = []
        parents = soup.findAll('div', 'row job-information')
        for parent in parents:
            try:
                temp = parent.find('div', 'columns large-2 medium-3 small-12').find('h4')
            except AttributeError:
                companies.append(None)
            else:
                if temp.a:
                    # Company name is sometimes wrapped in anchor tag
                    companies.append(temp.find('a').contents[0].strip())
                else:
                    companies.append(temp.contents[0].strip())
        return companies
