###
###This program computes the square root of a number after 2 different algorithms and displays them in a wanna be table
###

import math
import sys


# declared variables here
a1 = 1#float(input('a1 value '))
a2 = 2#float(input('a2 value '))
a3 = 3#float(input('a2 value '))
a4 = 4#float(input('a2 value '))
a5 = 5#float(input('a2 value '))
a6 = 6#float(input('a2 value '))
a7 = 7#float(input('a2 value '))
a8 = 8#float(input('a2 value '))



def mysqrt(a):  # this is the algorithm that computes the square root of a (Newtons method)
    x = 3
    while True:
        y = (x + a / x) / 2
        if y == x:
            break
        x = y
    return '{:<5}'.format(x)



def python_sqrt(a): #Python math bult-in function
    x = math.sqrt(a)
    return x


def diff(x, y):
    while True:
        if abs(y-x)< sys.float_info.epsilon:
            break
        return abs(y-x)


def space():  # this makes 5 empty string spaces
    x = '      '  # exactly 5 spaces
    return x


def space_2():  # this makes 5 empty string spaces
    x = '    '  # exactly 5 spaces
    return x


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


