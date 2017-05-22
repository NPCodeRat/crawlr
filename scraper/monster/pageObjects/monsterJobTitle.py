class MonsterJobTitle(object):
    """Pull job titles from Monster search"""

    @classmethod
    def pull_titles(cls, soup):
        titles = []
        parents = soup.findAll('div', 'jobTitle')
        for parent in parents:
            try:
                titles.append(parent.find('span').contents[0].strip())
            except AttributeError:
                titles.append(parent.find('span'))
        return titles
