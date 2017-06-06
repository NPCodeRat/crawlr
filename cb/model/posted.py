class Posted(object):
    """Enum for posting date query param, default to 30 days"""
    HOURS_24 = dict({'label': '24 hours', 'value': 'posted=1'})
    DAYS_3 = dict({'label': '3 days', 'value': 'posted=3'})
    DAYS_7 = dict({'label': '7 days', 'value': 'posted=7'})
    DAYS_30 = dict({'label': '30 days', 'value': None})

    @classmethod
    def append(cls):
        """Skip user input, default to 30 days"""
        return cls.DAYS_30.get('value')

    @classmethod
    def cmd_append(cls):
        """Prompt user for post-date input"""
        choice = raw_input(
            '*****\nSearch the past...\n\n1 - {}\n2 - {}\n3 - {}\n4 - {}\n\n'
                .format(cls.HOURS_24.get('label'), cls.DAYS_3.get('label'), cls.DAYS_7.get('label'),
                        cls.DAYS_30.get('label')))
        if choice == '1':
            return cls.HOURS_24.get('value')
        elif choice == '2':
            return cls.DAYS_3.get('value')
        elif choice == '3':
            return cls.DAYS_7.get('value')
        elif choice == '4':
            return cls.DAYS_30.get('value')
        else:
            print '\nNot an option.  Defaulting to 30 miles.\n'
            return cls.DAYS_30.get('value')
