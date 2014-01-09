days_in_month = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10: 31,
    11: 30,
    12: 31
}

def last_day_in_month(month, year):
    if month != 2:
        return days_in_month[month]
    elif year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        return 28
    else:
        return 29

class Sundays(object):
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def __repr__(self):
        return "{0}/{1}/{2}".format(self.month, self.day, self.year)

    def jump_to_next_sunday(self):
        if self.day + 7 <= last_day_in_month(self.month, self.year):
            self.day += 7
            return
        self.day = self.day + 7 - last_day_in_month(self.month, self.year)
        self.month = self.month % 12 + 1
        if self.month == 1:
            self.year += 1

s = Sundays(12, 30, 1900)
total = 0
while s.year < 2001:
    if s.day == 1:
        total += 1
    s.jump_to_next_sunday()

print(total)
