import datetime

YEARFINE = 10000
MONTHFINE = 500
DAYFINE = 15

[d1, m1, y1] = "1 1 2015".split()
[d2, m2, y2] = "31 12 2014".split()

returnedDate = datetime.date(int(y1), int(m1), int(d1))
expectedDate = datetime.date(int(y2), int(m2), int(d2))

diffDate = returnedDate - expectedDate
if diffDate <= datetime.timedelta(days=0):
    print 0
elif diffDate > datetime.timedelta(days=365):
    print YEARFINE
elif diffDate > datetime.timedelta(days=31):
    print MONTHFINE * ((int(m1) - int(m2)) % 12)
else:
    print DAYFINE * diffDate.days
