import math


class Point:
    """
    Represents a point in 2D space:
    attributes: x coordinate, y coordinate
    """


class Circle:
    """
    attributes: center, radius
    """
    center = Point()
    radius = float


class Rectangle:
    """Represents a rectangle.

    attributes: width, height, corner or center.
    """
    center = Point()
    corner = Point()
    width = float
    height = float

def distance (x1, y1, x2, y2):
    """
    this function returns the distance between 2 points
    """
    dx = x2-x1
    dy = y2-y1
    d_squared = dx ** 2 + dy ** 2
    result = math.sqrt(d_squared)
    return result


def create_point(x, y):
    point = Point()
    point.x = x
    point.y = y
    return point


def circle_creation(x, y, radius):
    circle = Circle()
    circle.center.x = x
    circle.center.y = y
    circle.radius = radius
    return circle


def rectangle_creation(x, y, width, height):
    rectangle = Rectangle()
    rectangle.corner.x = x
    rectangle.corner.y = y
    rectangle.width = width
    rectangle.height = height
    return rectangle


def point_in_circle(distance, radius):
    if distance < radius or distance == radius:
        print('Point lies on or inside the circle')
        return
    else:
        print('Point lies outside the circle')
        return


def find_center_rect(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p


def rectangle_in_circle(rect, circle):

    #  here we compute the coordinates
    #  for all the corners of the rectangle
    corner_top_left = (rect.corner.x, rect.corner.y)
    corner_top_right = (rect.corner.x + rect.width, rect.corner.y)
    corner_bottom_left = (rect.corner.x, rect.corner.y - rect.height)
    corner_bottom_right = (rect.corner.x + rect.width, rect.corner.y - rect.height)

    #  here we assign the coordinates for the circles center
    circle_center = (circle.center.x, circle.center.y)

    #  here we compute the distances from
    #  the circles center to all of the rectangles points
    distance_1 = distance(corner_top_left[0], corner_top_left[1], circle_center[0], circle_center[1])
    distance_2 = distance(corner_top_right[0], corner_top_right[1], circle_center[0], circle_center[1])
    distance_3 = distance(corner_bottom_left[0], corner_bottom_left[1], circle_center[0], circle_center[1])
    distance_4 = distance(corner_bottom_right[0], corner_bottom_right[1], circle_center[0], circle_center[1])

    #  here we compare if the distances from circle center
    #  to the rectangle corners are smaller
    #  than the circles radius
    list_distances = [distance_1, distance_2, distance_3, distance_4]
    for x in list_distances:
        if x < circle.radius:
            continue
        elif x == circle.radius:
            continue
        else:
            print("False! At least one corner lies outside the circle")
            return False
    print("True! All corners are inside the circle")
    return True


#  here in this section we check if given point is inside the circle
point_1 = create_point(200, 150)
print('Point coordinates: x: %g y: %g' % (point_1.x, point_1.y))
circle_1 = circle_creation(x=150, y=100, radius=75)
print('Circle center x: %g y: %g and radius %g' % (circle_1.center.x, circle_1.center.y, circle_1.radius))
distance_point_to_circle = distance(circle_1.center.x, circle_1.center.y, point_1.x, point_1.y)
print('Distance point to circle center: %g mm' % distance_point_to_circle)

point_in_circle(distance_point_to_circle, circle_1.radius)

#  here in this section we check if rectangle is inside the circle
box_1 = rectangle_creation(x=150, y=100, width=120, height=240)
rectangle_in_circle(box_1, circle_1)
