class Pay(object):
    """Enum for pay rate query param, defaults to any"""
    ANY = dict({'label': 'Any', 'value': None})
    OVER_20 = dict({'label': '$20,000+', 'value': 'pay=20'})
    OVER_40 = dict({'label': '$40,000+', 'value': 'pay=40'})
    OVER_60 = dict({'label': '$60,000+', 'value': 'pay=60'})
    OVER_80 = dict({'label': '$80,000+', 'value': 'pay=80'})
    OVER_100 = dict({'label': '$100,000+', 'value': 'pay=100'})
    OVER_120 = dict({'label': '$120,000+', 'value': 'pay=120'})

    @classmethod
    def append(cls):
        return cls.ANY.get('value')

    @classmethod
    def cmd_append(cls):
        choice = raw_input(
            '*****\nSearch for pay...\n\n1 - {}\n2 - {}\n3 - {}\n4 - {}\n5 - {}\n6 - {}\n7 - {}\n\n'
                .format(cls.ANY.get('label'), cls.OVER_20.get('label'), cls.OVER_40.get('label'),
                        cls.OVER_60.get('label'), cls.OVER_80.get('label'), cls.OVER_100.get('label'),
                        cls.OVER_120.get('label')))
        if choice == '1':
            return cls.ANY.get('value')
        elif choice == '2':
            return cls.OVER_20.get('value')
        elif choice == '3':
            return cls.OVER_40.get('value')
        elif choice == '4':
            return cls.OVER_60.get('value')
        elif choice == '5':
            return cls.OVER_80.get('value')
        elif choice == '6':
            return cls.OVER_100.get('value')
        elif choice == '7':
            return cls.OVER_120.get('value')
        else:
            print '\nNot an option.  Defaulting to any pay.\n'
            return cls.ANY.get('value')
