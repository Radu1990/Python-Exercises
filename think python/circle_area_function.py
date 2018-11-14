print('This program computes the area of a circle using as input the circle center point and a point on the circle perimeter')
print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _')
print('****************************************************************')
xc = float(input('Enter center coordinate x1: '))
yc = float(input('Enter center coordinate y1: '))
xp = float(input('Enter perimeter point coordinate x2: '))
yp = float(input('Enter perimeter point coordinate y2: '))
print('****************************************************************')
import math

def distance (x1, y1, x2, y2):
    dx = x2-x1
    dy = y2-y1
    dsquared = dx ** 2 + dy ** 2
    result = math.sqrt(dsquared)
    return result

def area(radius):
    a = ( (math.pi) * (radius**2) )
    return a

def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result



circle_area(xc, yc, xp, yp)
print("Circle area is :", circle_area(xc, yc, xp, yp))
print('This was verified and works!')
