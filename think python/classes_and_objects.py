import math


class Point:
    """
    Represents a point in 2D space:
    """


def point_creation(pos_x, pos_y):
    name_pct = Point()
    name_pct.x = pos_x
    name_pct.y = pos_y
    return name_pct


def print_point(p):
    return 'point (%g, %g)' % (p.x, p.y)


def distance_between_two_points(p1, p2):
    distance = math.sqrt((p2.x-p1.x)**2 + (p2.y-p1.y)**2)
    return distance


p1 = point_creation(pos_x=3, pos_y=4)
p2 = point_creation(pos_x=15, pos_y=80)

print('Distance between %s and %s is %g' % (print_point(p1), print_point(p2), distance_between_two_points(p1, p2)))
