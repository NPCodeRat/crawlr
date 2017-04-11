from enum import Enum
import urllib


class Emp(Enum):
    """Enum for employment type query param, default to all types"""
    FULL_TIME = 'jtft,jtfp'
    PART_TIME = 'jtpt,jtfp'
    CONTRACT = 'jtct'
    CONTRACT_TO_HIRE = 'jtch'
    INTERN = 'jtin'
    SEASONAL = 'jtse'

    def __str__(self):
        if self.value == 'jtft,jtfp':
            return 'full time'
        if self.value == 'jtpt,jtfp':
            return 'part time'
        if self.value == 'jtct':
            return 'contract'
        if self.value == 'jtch':
            return 'contract to hire'
        if self.value == 'jtin':
            return 'intern'
        if self.value == 'jtse':
            return 'seasonal'

    def __eq__(self, y):
        return self.value == y.value

    __repr__ = __str__

    @staticmethod
    def append():
        print 'None'
        return None

    @staticmethod
    def cmd_append():
        repeat = 'y'
        query_set = []
        while repeat == 'y':
            choice = raw_input(
                '*****\nSearch for what type of employment?\n\n1 - {}\n2 - {}\n3 - {}\n4 - {}\n5 - {}\n6 - {}\n\n'
                    .format(Emp.FULL_TIME, Emp.PART_TIME, Emp.CONTRACT, Emp.CONTRACT_TO_HIRE,
                            Emp.INTERN, Emp.SEASONAL))
            if choice == '1':
                query_set.append(Emp.FULL_TIME)
            elif choice == '2':
                query_set.append(Emp.PART_TIME)
            elif choice == '3':
                query_set.append(Emp.CONTRACT)
            elif choice == '4':
                query_set.append(Emp.CONTRACT_TO_HIRE)
            elif choice == '5':
                query_set.append(Emp.INTERN)
            elif choice == '6':
                query_set.append(Emp.SEASONAL)
            else:
                print '\nNot an option'
            repeat = raw_input('\nAdd more employment types to search? (y/n)\n')
        return query_set

    @staticmethod
    def get_formatted():
        unformatted = []
        base = Emp.cmd_append()
        for query in base:
            unformatted.append(query.value)
        return "emp=" + urllib.quote_plus(",".join(map(str, list(set(unformatted)))))
