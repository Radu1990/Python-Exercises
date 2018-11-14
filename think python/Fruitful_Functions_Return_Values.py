print('*****************************************************************************************')
print('this will print circle area')
print('*****************************************************************************************')

import math
radius = int( input("Enter Radius: ") )
def area(radius):
    a = ( (math.pi) * (radius**2) )
    return a
area(radius)

print("Circle area: ", area(radius))

#

def absolute_value(radius):
    n = radius
    if n < 0:
        return (-n)
    else:
        return (n)
absolute_value(radius)
print('Absolute value of radius value is:', absolute_value(radius))

print('*****************************************************************************************')
print('Now we compare some numbers...')
print('*****************************************************************************************')

x = input('Specify x: ')
y = input('Specify y: ')

def compare_values(x,y):
    if x > y:
        return 1
    if x == y:
        return 0
    if x < y:
        return -1
compare_values(x,y)
print('*****************************************************************************************')
print('Legend:\n***\nx>y = 1\nx == y = 0\nx<y = -1\n***\nComparison result: ', compare_values(x,y) )
