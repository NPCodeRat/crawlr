class PostTime(object):
    """Pull posting times from CB search"""
    PARENT = dict({'tag': 'div', 'class': 'time-posted'})

    @classmethod
    def pull_times(cls, soup):
        times = []
        rows = soup.findAll(cls.PARENT.get('tag'), cls.PARENT.get('class'))
        for row in rows:
            times.append(row.find('div', 'show-for-medium-up').em.contents[0].strip())
        return times
