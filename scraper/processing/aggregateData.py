from scraper.cb.pageObjects.address import Address
from scraper.cb.pageObjects.company import Company
from scraper.cb.pageObjects.distance import Distance
from scraper.cb.pageObjects.fullPart import FullPart
from scraper.cb.pageObjects.jobDesc import JobDesc
from scraper.cb.pageObjects.jobTitle import JobTitle
from scraper.cb.pageObjects.postTime import PostTime


class AggregateData(object):
    """Pull all data from beautiful soups, format for CSV processing"""

    @classmethod
    def pull_all(cls, soups):
        title, description, time, type, pay, distance, company, address = [], [], [], [], [], [], [], []
        for soup in soups:
            title += JobTitle.pull_titles(soup)
            description += JobDesc.pull_descriptions(soup)
            time += PostTime.pull_times(soup)
            type += FullPart.pull_employment_info(soup).get('info')
            pay += FullPart.pull_employment_info(soup).get('pay')
            distance += Distance.pull_distance(soup)
            company += Company.pull_companies(soup)
            address += Address.pull_addresses(soup)
        length = len(title)
        for lst in [description, time, type, pay, distance, company, address]:
            if len(lst) != length:
                raise ArithmeticError('Inaccurate data: mismatched indices')
        processed_data = []
        for x in range(0, len(title)):
            temp = [title[x], description[x], time[x], type[x], pay[x], distance[x], company[x], address[x]]
            processed_data.append(temp)
        print processed_data
