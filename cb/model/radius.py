class Radius(object):
    """Enum for distance query param, default to 30 miles"""
    MILES_5 = dict({'label': 'five miles', 'value': 'radius=5'})
    MILES_10 = dict({'label': 'ten miles', 'value': 'radius=10'})
    MILES_30 = dict({'label': 'thirty miles', 'value': None})
    MILES_50 = dict({'label': 'fifty miles', 'value': 'radius=50'})

    @classmethod
    def append(cls):
        return cls.MILES_30.get('value')

    @classmethod
    def cmd_append(cls):
        choice = raw_input(
            '*****\nSearch surrounding...\n\n1 - {}\n2 - {}\n3 - {}\n4 - {}\n\n'
                .format(cls.MILES_5.get('label'), cls.MILES_10.get('label'), cls.MILES_30.get('label'),
                        cls.MILES_50.get('label')))
        if choice == '1':
            print cls.MILES_5.get('value')
            return cls.MILES_5.get('value')
        elif choice == '2':
            print cls.MILES_10.get('value')
            return cls.MILES_10.get('value')
        elif choice == '3':
            print cls.MILES_30.get('value')
            return cls.MILES_30.get('value')
        elif choice == '4':
            print cls.MILES_50.get('value')
            return cls.MILES_50.get('value')
        else:
            print '\nNot an option.  Defaulting to 30 miles.\n'
            print cls.MILES_30.get('value')
            return cls.MILES_30.get('value')
