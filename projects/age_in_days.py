"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.

Code saved in http://py3.codeskulptor.org/#user301_BA76ZMf9sL_0.py
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if month != 12:
        date_reference = datetime.date(year, month, 1)
        date_next_month = datetime.date(year, month + 1, 1)
        diff = date_next_month - date_reference
        return diff.days
    else:
        return 31   

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    is_valid_year = year in range(datetime.MINYEAR, datetime.MAXYEAR + 1)
    is_valid_month = month in range(1, 12 + 1)

    if is_valid_year and is_valid_month:
        if day in range(1, days_in_month(year, month) + 1):
            return True
    
    return False

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    is_valid_date1 = is_valid_date(year1, month1, day1)
    is_valid_date2 = is_valid_date(year2, month2, day2)
    if is_valid_date1 and is_valid_date2:
        date1 = datetime.date(year1, month1, day1)
        date2 = datetime.date(year2, month2, day2)
        diff = date2 - date1
        if diff.days > 0:
            return diff.days
    
    return 0

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    today = datetime.date.today()
    return days_between(year, month, day, today.year, today.month, today.day)


print("# Testing days_in_month():")
print("2018/2 has 28 days?:", days_in_month(2018, 2) == 28)
print("2018/3 has 31 days?:", days_in_month(2018, 3) == 31)
print("2018/4 has 30 days?:", days_in_month(2018, 4) == 30)
print("2018/12 has 31 days?:", days_in_month(2018, 12) == 31)
print("9999/12 has 31 days?:", days_in_month(9999, 12) == 31) # test to prevent error: year 1000 is out of range
print()

print("# Testing is_valid_date():")
print("day 30/2 is invalid?: ", is_valid_date(2018, 2, 30) == False)
print("day zero is invalid?:", is_valid_date(2018, 2, 0) == False)
print("year (MINYEAR - 1) is invalid?", is_valid_date(datetime.MINYEAR - 1, 12, 1) == False)
print("year (MAXYEAR + 1) is invalid?", is_valid_date(datetime.MAXYEAR + 1, 12, 1) == False)
print("month 13 is invalid?", is_valid_date(2018, 13, 1) == False)
print("month 0 is invalid?", is_valid_date(2018, 0, 1) == False)
print("1/1/1 is valid?:", is_valid_date(1, 1, 1))
print("2018/5/5 is valid?:", is_valid_date(2018, 5, 5))
print("9999/12/31 is valid?:", is_valid_date(9999, 12, 31))
print()

print("# Testing days_between():")
print("When invalid date1 return 0?: ", days_between(0, 1, 90, 2018, 1, 1) == 0)
print("When date2 return 0?: ", days_between(2018, 1, 1, 0, 1, 1) == 0)
print("When date2 before date1 return 0?: ", days_between(2018, 2, 2, 2018, 1, 1) == 0)
print("There is 1 day between 2018-01-01 and 2018-01-02?: ", days_between(2018, 1, 1, 2018, 1, 2) == 1)
print("There is 30 day between 2018-01-01 and 2018-01-31?: ", days_between(2018, 1, 1, 2018, 1, 31) == 30)
print("There is 32 day between 2018-01-01 and 2018-02-02?: ", days_between(2018, 1, 1, 2018, 2, 2) == 32)
print()

print("# Testing age_in_days():")
print(age_in_days(2018, 6, 6))
print(age_in_days(2018, 6, 5))
print(age_in_days(2000, 6, 5))
print(age_in_days(1991, 1, 27))
print("Date in future returns: ", age_in_days(9999, 6, 5))
print("Date in invalid returns: ", age_in_days(0, 6, 45))
