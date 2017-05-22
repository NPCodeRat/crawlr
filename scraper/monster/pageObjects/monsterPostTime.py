class MonsterPostTime(object):
    """Pull post times from Monster search"""

    @classmethod
    def pull_times(cls, soup):
        times = []
        parents = soup.findAll('time')
        for parent in parents:
            try:
                times.append(parent.contents[0].strip())
            except AttributeError:
                times.append(parent)
        return times
