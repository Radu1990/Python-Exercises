import math
print('This program computes the length of a hypotenuse using catete lengths as input')
print('******************************************************************************')
a = float(input('a length: '))
b = float(input('b length: '))

def hypotenuse(a,b):
    c = math.sqrt(a**2 + b**2)
    return c

hypotenuse(a,b)
print('Results is: ', hypotenuse(a,b))


