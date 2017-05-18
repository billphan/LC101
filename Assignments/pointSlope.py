class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    # TODO define a method called slopeFromOrigin here
    
    # define a funcion called 'slopeFromOrigin' taking 'self' as a parameter.
    def slopeFromOrigin(self):
        # if self method x == 0
        if self.x == 0:
            # return None if divided by 0
            return None
        # else return y / x
        return self.y / self.x

# some tests to check your code
from test import testEqual
testEqual( Point(4, 10).slopeFromOrigin(), 2.5 )
testEqual( Point(5, 10).slopeFromOrigin(), 2 )
testEqual( Point(0, 10).slopeFromOrigin(), None )
testEqual( Point(20, 10).slopeFromOrigin(), 0.5 )
testEqual( Point(20, 20).slopeFromOrigin(), 1 )
testEqual( Point(4, -10).slopeFromOrigin(), -2.5 )
testEqual( Point(-4, -10).slopeFromOrigin(), 2.5 )
testEqual( Point(-6, 0).slopeFromOrigin(), 0 )
