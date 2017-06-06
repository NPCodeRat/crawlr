class FullPart(object):
    """Pull full-time / part-time / etc info from CB search"""

    @classmethod
    def pull_employment_info(cls, soup):
        """Find all compensation and full vs. part time employment data in provided soup"""
        infos = []
        pays = []
        rows = soup.findAll('h4', 'job-text employment-info')
        for row in rows:
            temp = row.contents[0].strip()
            if temp.find('|') > -1:
                # Element may contain both compensation and employment type data
                data = temp.split(' | Pay: ')
                # If two values are provided, they will be separated by a pipechar
                infos.append(data[0])
                pays.append(data[1])
            else:
                infos.append(temp)
                pays.append(None)
        return dict({'info': infos, 'pay': pays})
