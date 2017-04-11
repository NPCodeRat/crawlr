from enum import Enum


class Posted(Enum):
    """Enum for posting date query param, default to 30 days"""
    HOURS_24 = "posted=1"
    DAYS_3 = "posted=3"
    DAYS_7 = "posted=7"
    DAYS_30 = None

    def __str__(self):
        if self.value == 'posted=1':
            return '24 hours'
        if self.value == 'posted=3':
            return '3 days'
        if self.value == 'posted=7':
            return '7 days'
        if not self.value:
            return '30 days'

    def __eq__(self, y):
        return self.value == y.value

    __repr__ = __str__

    @staticmethod
    def append():
        return Posted.DAYS_30

    @staticmethod
    def cmd_append():
        choice = raw_input(
            '*****\nSearch the past...\n\n1 - {}\n2 - {}\n3 - {}\n4 - {}\n\n'
                .format(Posted.HOURS_24, Posted.DAYS_3,
                        Posted.DAYS_7, Posted.DAYS_30))
        if choice == '1':
            return Posted.HOURS_24
        elif choice == '2':
            return Posted.DAYS_3
        elif choice == '3':
            return Posted.DAYS_7
        elif choice == '4':
            return Posted.DAYS_30
        else:
            print '\nNot an option.  Defaulting to 30 miles.\n'
            return Posted.DAYS_30
