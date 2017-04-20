class JobTitle(object):
    """Pull job titles from CB search"""
    PARENT = dict({'tag': 'h2', 'class': 'job-title'})

    @classmethod
    def pull_titles(cls, soup):
        titles = []
        rows = soup.findAll(cls.PARENT.get('tag'), cls.PARENT.get('class'))
        for row in rows:
            titles.append(row.find('a').contents[0].strip())
        return titles
