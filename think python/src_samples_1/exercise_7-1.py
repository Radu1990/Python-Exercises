import math
import sys

"""
    This program computes the square root of a number
    after 2 different algorithms and displays them in a table
    
    Input:  
        a1, a2, ... , an.
    Output:
          a     mysqrt(a)            math.sqrt(a)        
          -     ---------            ------------        
          1     1.0                  1.0                 
          2     1.414213562373095    1.4142135623730951  
          3     1.7320508075688772   1.7320508075688772  
          4     2.0                  2.0                 
          5     2.23606797749979     2.23606797749979    
          6     2.449489742783178    2.449489742783178   
          7     2.6457513110645907   2.6457513110645907  
          8     2.82842712474619     2.8284271247461903  
"""

# declared variables here
a1 = 1
a2 = 2
a3 = 3
a4 = 4
a5 = 5
a6 = 6
a7 = 7
a8 = 8


# this is the algorithm that computes
# the square root of 'a' (Newtons method)
def mysqrt(a):
    x = 3
    while True:
        y = (x + a / x) / 2
        if y == x:
            break
        x = y
    return '{:<5}'.format(x)


# Python math bult-in function
def python_sqrt(a):
    x = math.sqrt(a)
    return x


def diff(x, y):
    while True:
        if abs(y-x)< sys.float_info.epsilon:
            break
        return abs(y-x)


def test_square_root():
    print('{:<5}'.format('a'), '{:<20}'.format('mysqrt(a)'), '{:<20}'.format('math.sqrt(a)'))
    print('{:<5}'.format('-'), '{:<20}'.format('---------'), '{:<20}'.format('------------'))
    print('{:<5}'.format(a1), '{:<20}'.format(mysqrt(a1)), '{:<20}'.format(python_sqrt(a1)))
    print('{:<5}'.format(a2), '{:<20}'.format(mysqrt(a2)), '{:<20}'.format(python_sqrt(a2)))
    print('{:<5}'.format(a3), '{:<20}'.format(mysqrt(a3)), '{:<20}'.format(python_sqrt(a3)))
    print('{:<5}'.format(a4), '{:<20}'.format(mysqrt(a4)), '{:<20}'.format(python_sqrt(a4)))
    print('{:<5}'.format(a5), '{:<20}'.format(mysqrt(a5)), '{:<20}'.format(python_sqrt(a5)))
    print('{:<5}'.format(a6), '{:<20}'.format(mysqrt(a6)), '{:<20}'.format(python_sqrt(a6)))
    print('{:<5}'.format(a7), '{:<20}'.format(mysqrt(a7)), '{:<20}'.format(python_sqrt(a7)))
    print('{:<5}'.format(a8), '{:<20}'.format(mysqrt(a8)), '{:<20}'.format(python_sqrt(a8)))


test_square_root()

