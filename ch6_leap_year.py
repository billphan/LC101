'''
A year is a leap year if it is divisible by 4, unless it is a century that is not divisible by 400.

For example:

1956 is a leap year because 1956 is divisible by 4.
1957 is not a leap year, because it is not divisible by 4.
1900 is not a leap year, despite the fact that it is divisible by 4, because 1900 is a century and 1900 is not divisible by 400.
1600 is a leap year, because 1600 is divisible by 4 and 1600 is divisible by 400
Write a function isLeap that takes a year as a parameter and returns True if the year is a leap year, False otherwise.
'''

def isLeap(year):
    # your code here
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False
