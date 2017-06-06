class Rad(object):
    """Enum for rad query param, default to 5 miles"""
    MILES_5 = dict({'label': 'five miles', 'value': 'rad=5'})
    MILES_10 = dict({'label': 'ten miles', 'value': 'rad=10'})
    MILES_20 = dict({'label': 'twenty miles', 'value': 'rad=20'})
    MILES_30 = dict({'label': 'thirty miles', 'value': 'rad=30'})
    MILES_40 = dict({'label': 'forty miles', 'value': 'rad=40'})
    MILES_50 = dict({'label': 'fifty miles', 'value': 'rad=50'})
    MILES_60 = dict({'label': 'sixty miles', 'value': 'rad=60'})
    MILES_75 = dict({'label': 'seventy five miles', 'value': 'rad=75'})
    MILES_100 = dict({'label': 'one hundred miles', 'value': 'rad=100'})
    MILES_150 = dict({'label': 'one hundred fifty miles', 'value': 'rad=150'})
    MILES_200 = dict({'label': 'two hundred miles', 'value': 'rad=200'})

    @classmethod
    def append(cls):
        """Skip user input, default to 5 miles"""
        return cls.MILES_5.get('value')

    @classmethod
    def cmd_append(cls):
        """Prompt user for search radius input"""
        choice = raw_input(
            '*****\nSearch surrounding...\n\n1 - {}\n2 - {}\n3 - {}\n4 - {}\n'
            '5 - {}\n6 - {}\n7 - {}\n8 - {}\n9 - {}\n10 - {}\n11 - {}\n\n'.format(
                cls.MILES_5.get('label'), cls.MILES_10.get('label'), cls.MILES_20.get('label'),
                cls.MILES_30.get('label'), cls.MILES_40.get('label'), cls.MILES_50.get('label'),
                cls.MILES_60.get('label'), cls.MILES_75.get('label'), cls.MILES_100.get('label'),
                cls.MILES_150.get('label'), cls.MILES_200.get('label')
            )
        )
        if choice == '1':
            return cls.MILES_5.get('value')
        elif choice == '2':
            return cls.MILES_10.get('value')
        elif choice == '3':
            return cls.MILES_20.get('value')
        elif choice == '4':
            return cls.MILES_30.get('value')
        elif choice == '5':
            return cls.MILES_40.get('value')
        elif choice == '6':
            return cls.MILES_50.get('value')
        elif choice == '7':
            return cls.MILES_60.get('value')
        elif choice == '8':
            return cls.MILES_75.get('value')
        elif choice == '9':
            return cls.MILES_100.get('value')
        elif choice == '10':
            return cls.MILES_150.get('value')
        elif choice == '11':
            return cls.MILES_200.get('value')
        else:
            print '\nNot an option.  Defaulting to 5 miles.\n'
            return cls.MILES_5.get('value')
