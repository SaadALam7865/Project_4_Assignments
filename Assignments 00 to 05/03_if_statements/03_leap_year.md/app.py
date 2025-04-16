# Write a program that reads a year from the user and tells whether a given year is a leap year or not.
# A leap year (also known as an intercalary year or bissextile year) is a calendar year that contains an additional day (or, in the case of a lunisolar calendar, a month) added to keep the calendar year synchronized with the astronomical year or seasonal year. In the Gregorian calendar, each leap year has 366 days instead of 365, by extending February to 29 days rather than the common 28.
# In the Gregorian calendar, three criteria must be checked to identify leap years:
# The given year must be evenly divisible by 4;
# If the year can also be evenly divided by 100, it is NOT a leap year; unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# Your code should use the above criteria to check for a leap year and then print either "That's a leap year!" or "That's not a leap year."

def is_leap_year(year):
    """
    Check if a given year is a leap year.
    """
    if year % 4 != 0:
        return False
    elif year % 100 == 0:
        return year % 400 == 0
    else:
        return True

# Get the year from the user
year = int(input('Enter a year: '))

# Check if the year is a leap year
if is_leap_year(year):
    print("That's a leap year!")
else:
    print("That's not a leap year.")

if __name__ == '__main__':
    # Test the function with some sample inputs
    assert is_leap_year(2000) == True, "Test case 1 failed"
    assert is_leap_year(1900) == False, "Test case 2 failed"
    assert is_leap_year(2004) == True, "Test case 3 failed"
    assert is_leap_year(2001) == False, "Test case 4 failed"
    assert is_leap_year(2020) == True, '"Test case 5 failed"'
    print("All test cases passed!")



