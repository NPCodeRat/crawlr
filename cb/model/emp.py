import urllib


class Emp(object):
    """Enum for employment type query param, default to all types"""
    ANY = dict({'label': 'any', 'value': None})
    FULL_TIME = dict({'label': 'full time', 'value': 'jtft,jtfp'})
    PART_TIME = dict({'label': 'part time', 'value': 'jtpt,jtfp'})
    CONTRACT = dict({'label': 'contract', 'value': 'jtct'})
    CONTRACT_TO_HIRE = dict({'label': 'contract to hire', 'value': 'jtch'})
    INTERN = dict({'label': 'intern', 'value': 'jtin'})
    SEASONAL = dict({'label': 'seasonal', 'value': 'jtse'})

    @classmethod
    def append(cls):
        """Skip user input, default to all types"""
        return None

    @classmethod
    def cmd_append(cls):
        """Prompt user for employment type input"""
        repeat = 'y'
        query_set = list()
        # Allow for multiple employment type choices per search
        while repeat == 'y':
            choice = raw_input(
                '*****\nSearch for what type of employment?\n\n1 - {}\n2 - {}\n3 - {}\n4 - {}\n5 - {}\n6 - {}\n7 - {}\n\n'
                    .format(cls.ANY.get('label'), cls.FULL_TIME.get('label'), cls.PART_TIME.get('label'),
                            cls.CONTRACT.get('label'), cls.CONTRACT_TO_HIRE.get('label'), cls.INTERN.get('label'),
                            cls.SEASONAL.get('label')))
            if choice == '1':
                del query_set[:]
                query_set.append(cls.ANY.get('value'))
                break
            elif choice == '2':
                query_set.append(cls.FULL_TIME.get('value'))
            elif choice == '3':
                query_set.append(cls.PART_TIME.get('value'))
            elif choice == '4':
                query_set.append(cls.CONTRACT.get('value'))
            elif choice == '5':
                query_set.append(cls.CONTRACT_TO_HIRE.get('value'))
            elif choice == '6':
                query_set.append(cls.INTERN.get('value'))
            elif choice == '7':
                query_set.append(cls.SEASONAL.get('value'))
            else:
                print '\nNot an option'
            repeat = raw_input('\nAdd more employment types to search? (y/n)\n')
        return query_set

    @classmethod
    def get_formatted(cls):
        """Restructure user choices as a string to be used in request URL"""
        unformatted = []
        base = cls.cmd_append()
        for query in base:
            if query:
                unformatted.append(query)
        if len(unformatted) != 0:
            # CB API expects comma separated list of employment types
            return "emp=" + urllib.quote_plus(",".join(map(str, list(set(unformatted)))))
        else:
            return None
