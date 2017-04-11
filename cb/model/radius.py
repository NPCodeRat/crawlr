from enum import Enum


class Radius(Enum):
    """Enum for distance query param, default to 30 miles"""
    MILES_5 = 'radius=5'
    MILES_10 = 'radius=10'
    MILES_30 = None
    MILES_50 = 'radius=50'

    def __str__(self):
        if self.value == 'radius=5':
            return 'five miles'
        if self.value == 'radius=10':
            return 'ten miles'
        if not self.value:
            return 'thirty miles'
        if self.value == 'radius=50':
            return 'fifty miles'

    def __eq__(self, y):
        return self.value == y.value

    __repr__ = __str__

    @staticmethod
    def append():
        print 'None'
        return None

    @staticmethod
    def cmd_append():
        choice = raw_input(
            '*****\nSearch surrounding...\n\n1 - {}\n2 - {}\n3 - {}\n4 - {}\n\n'
                .format(Radius.MILES_5, Radius.MILES_10, Radius.MILES_30,
                        Radius.MILES_50))
        if choice == '1':
            print Radius.MILES_5
            return Radius.MILES_5
        elif choice == '2':
            print Radius.MILES_10
            return Radius.MILES_10
        elif choice == '3':
            print Radius.MILES_30
            return Radius.MILES_30
        elif choice == '4':
            print Radius.MILES_50
            return Radius.MILES_50
        else:
            print '\nNot an option.  Defaulting to 30 miles.\n'
