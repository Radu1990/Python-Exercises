import math
print('****************************************************************')
print('This function computes the distance between 2 points in 2D Space')
print('****************************************************************')
x1 = float(input('Enter x1: '))
y1 = float(input('Enter y1: '))
x2 = float(input('Enter x2: '))
y2 = float(input('Enter y2: '))
print('****************************************************************')
def distance (x1, y1, x2, y2):
    dx = x2-x1
    dy = y2-y1
    dsquared = dx ** 2 + dy ** 2
    result = math.sqrt(dsquared)
    return result

distance(x1, y1, x2, y2)
print(distance(x1, y1, x2, y2))
print("Done! :)")
