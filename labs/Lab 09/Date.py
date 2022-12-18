'''
Start to the Date class for Lab 9.  This code will not run in Python
until three methods are added:
    __init__,
    __str__
    same_day_in_year
'''

days_in_month = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July',\
                    'August','September', 'October', 'November', 'December' ]

class Date(object):
    def __init__(self, year=1990, month=1, day=1):
       self.y = year
       self.m = month
       self.d = day
    def __str__(self):
        stry = str(self.y)
        strm = str(self.m).rjust(2,'0')
        strd = str(self.d).rjust(2,'0')
        return '{}/{}/{}'.format(stry, strm, strd)
    def same_day_in_year(self, other):
        if (isinstance(other, Date)):
            if self.y == other.y:
                return True
            else:
                return False
    def is_leap_year(self):
        if self.y % 4 == 0:
            return True
        else:
            return False
    def __lt__(self, other):
        if self.y < other.y:
           return True
        elif self.y == other.y:
           if self.m < other.m:
               return True
           elif self.m == other.m and self.d < other.d:
               return True
           else:
               return False
        else:
            return False
           

if __name__ == "__main__":
    d1y = int(input("Please enter the year for the first date: "))
    d1m = int(input("Please enter the month for the first date: "))
    d1d = int(input("Please enter the day for the first date: "))
    
    d2y = int(input("Please enter the year for the second date: "))
    d2m = int(input("Please enter the month for the second date: "))
    d2d = int(input("Please enter the day for the second date: "))
    
    d3y = int(input("Please enter the year for the third date: "))
    d3m = int(input("Please enter the month for the third date: "))
    d3d = int(input("Please enter the day for the third date: "))
    
    d1 = Date(d1y, d1m, d1d)
    d2 = Date(d2y, d2m, d2d)
    d3 = Date(d3y, d3m, d3d)
    print("d1: " + str(d1))
    print("d2: " + str(d2))
    print("d3: " + str(d3))
    print("d1.same_day_in_year(d2)", d1.same_day_in_year(d2))
    print("d2.same_day_in_year(d3)", d2.same_day_in_year(d3)) 
    print ()
    print("Is d1 a leap year?", d1.is_leap_year())
    print("Is d2 a leap year?", d2.is_leap_year())
    print()
    print('d1 < d2', d1 < d2)
    print('d2 < d3', d2 < d3)
    print('d1 < d2', d1 < d2)

    