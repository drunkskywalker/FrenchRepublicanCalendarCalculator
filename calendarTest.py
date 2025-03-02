from republicanCalendar import *
import datetime

today = date.today()


print("autumn equinox:", getAutumnEquinox(today))

thisYear = getNewYearDate(today)
print("day of new year, today:", thisYear)
print("day of new year, previous day of new year:", getNewYearDate(date(thisYear.year, thisYear.month, thisYear.day - 1)))
print("day of new year, this year's autumn equinox:", getNewYearDate(getAutumnEquinox(today)))
assert(getNewYearDate(getAutumnEquinox(today)) == getAutumnEquinox(today))

print("first new year of FRC:", getFirstNewYearDate())
print("what year is first new year of FRC:", getYear(getFirstNewYearDate()))

nextYear = getAutumnEquinox(today)
nextYear_dayOffset1 = nextYear + datetime.timedelta(days=1)
print("next new year + 1 day:", nextYear_dayOffset1)
nextYear_p1 = getAutumnEquinox(nextYear_dayOffset1)
print("next new year + 1 day's next autumn equinox:", nextYear_p1)
print(nextYear_p1 - nextYear)
print("next new year is :", getYear(nextYear))
print("next 2 new year is:", getYear(nextYear_p1))

print("this year has days:", daysInYear(today))

print("is this year leap:", isLeap(today))
print("is next year leap:", isLeap(nextYear))

print("days since new year:", daysSinceNewYear(today))
print("month:", getMonthsSinceNewYear(today))

for i in range(12):
    assert(len(getDaysChinese()[i]) == 30)
assert(len(getDaysChinese()[12]) == 6)
assert(len(getDaysChinese()) == 13)
print("today is:", getRepublicanCalendarDayInChinese(today))
assert(getRepublicanCalendarTodayInChinese() == getRepublicanCalendarDayInChinese(today))


x = ephem.next_autumn_equinox(today)
print(type(x))

ephem.Date()