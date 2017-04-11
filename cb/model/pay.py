from enum import Enum


class Pay(Enum):
    """Enum for pay rate query param, defaults to any"""
    ANY = None
    OVER_20 = "pay=20"
    OVER_40 = "pay=40"
    OVER_60 = "pay=60"
    OVER_80 = "pay=80"
    OVER_100 = "pay=100"
    OVER_120 = "pay=120"

    def __str__(self):
        if not self.value:
            return 'Any'
        if self.value == 'pay=20':
            return '$20,000+'
        if self.value == 'pay=40':
            return '$40,000+'
        if self.value == 'pay=60':
            return '$60,000+'
        if self.value == 'pay=80':
            return '$80,000+'
        if self.value == 'pay=100':
            return '$100,000+'
        if self.value == 'pay=120':
            return '$120,000+'

    def __eq__(self, y):
        return self.value == y.value

    __repr__ = __str__

    @staticmethod
    def append():
        return Pay.ANY

    @staticmethod
    def cmd_append():
        choice = raw_input(
            '*****\nSearch for pay...\n\n1 - {}\n2 - {}\n3 - {}\n4 - {}\n5 - {}\n6 - {}\n7 - {}\n\n'
                .format(Pay.ANY, Pay.OVER_20, Pay.OVER_40, Pay.OVER_60,
                        Pay.OVER_80, Pay.OVER_100, Pay.OVER_120))
        if choice == '1':
            print Pay.ANY
            return Pay.ANY
        elif choice == '2':
            print Pay.OVER_20
            return Pay.OVER_20
        elif choice == '3':
            print Pay.OVER_40
            return Pay.OVER_40
        elif choice == '4':
            print Pay.OVER_60
            return Pay.OVER_60
        elif choice == '5':
            print Pay.OVER_80
            return Pay.OVER_80
        elif choice == '6':
            print Pay.OVER_100
            return Pay.OVER_100
        elif choice == '7':
            print Pay.OVER_120
            return Pay.OVER_120
        else:
            print '\nNot an option.  Defaulting to any pay.\n'
            return Pay.ANY
