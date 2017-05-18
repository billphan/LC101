'''
Write a function areaOfCircle(r) which returns the area of a circle of radius r

As a refresher, the area of any circle is equal to the radius squared, multiplied by pi (where pi is 3.14159....).

Don’t forget to include the math module, where pi is defined.
'''

# TODO: use def to define a function called areaOfCircle which takes an argument called r
# TODO implment your function to return the area of a circle whose radius is r

import math

def areaOfCircle(r):
    area = math.pi * r ** 2
    return area

areaOfCircle(0)
