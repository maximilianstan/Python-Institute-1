def isYearLeap(year):
    if year < 1582:
        return False
    elif year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def daysInMonth(year, month):
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isYearLeap(year) and month == 2:
        return 29
    return monthDays[month - 1]


def dayOfYear(year, month, day):
    # Validate inputs
    if year < 1582:
        return None
    if month > 12 or month < 1:
        return None
    if day > 31 or day < 1:
        return None

    # Calculate days
    totalDays = day
    month = month - 1
    while month > 0:
        totalDays += daysInMonth(year, month)
        month -= 1

    return totalDays


print(dayOfYear(2016, 12, 31))

print(dayOfYear(2015, 10, 5))