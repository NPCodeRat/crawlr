class JobDesc(object):
    """Pull descriptions from CB search"""

    @classmethod
    def pull_descriptions(cls, soup):
        """Find all job description data in provided soup"""
        descriptions = []
        rows = soup.findAll('div', 'job-description show-for-medium-up')
        for row in rows:
            descriptions.append(row.contents[0].strip())
        return descriptions
