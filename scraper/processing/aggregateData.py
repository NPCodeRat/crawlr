from scraper.cb.pageObjects.address import Address
from scraper.cb.pageObjects.company import Company
from scraper.cb.pageObjects.distance import Distance
from scraper.cb.pageObjects.fullPart import FullPart
from scraper.cb.pageObjects.jobDesc import JobDesc
from scraper.cb.pageObjects.jobTitle import JobTitle
from scraper.cb.pageObjects.postTime import PostTime
from scraper.monster.pageObjects.monsterAddress import MonsterAddress
from scraper.monster.pageObjects.monsterJobTitle import MonsterJobTitle
from scraper.monster.pageObjects.monsterCompany import MonsterCompany
from scraper.monster.pageObjects.monsterPostTime import MonsterPostTime


class AggregateData(object):
    """Pull all data from beautiful soups, format for CSV processing"""

    @classmethod
    def pull_all(cls, soups):
        title, description, time, type, pay, distance, company, address = [], [], [], [], [], [], [], []
        print 'Processing CareerBuilder data...'
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
        processed_data = [['Job Title', 'Job Description', 'Time Posted', 'Full / Part', 'Pay', 'Distance',
                          'Company', 'Location']]
        for x in range(0, len(title)):
            temp = [title[x], description[x], time[x], type[x], pay[x], distance[x], company[x], address[x]]
            processed_data.append(temp)
        print 'CareerBuilder data processed'
        return processed_data

    @classmethod
    def pull_monster(cls, soups):
        title, company, location, time = [], [], [], []
        print 'Processing Monster data...'
        for soup in soups:
            title += MonsterJobTitle.pull_titles(soup)
            company += MonsterCompany.pull_companies(soup)
            location += MonsterAddress.pull_addresses(soup)
            time += MonsterPostTime.pull_times(soup)
        length = len(title)
        for lst in [company, location, time]:
            if len(lst) != length:
                raise ArithmeticError('Inaccurate data: mismatched indices')
        processed_data = [['Job Title', 'Company', 'Location', 'Time Posted']]
        for x in range(0, len(title)):
            temp = [title[x], company[x], location[x], time[x]]
            processed_data.append(temp)
        print 'Monster data processed'
        return processed_data
