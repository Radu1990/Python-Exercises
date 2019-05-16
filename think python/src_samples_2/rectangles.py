import copy


class Point:
    """
    Represents a point in 2D space:

    attributes: x coordinate, y coordinate
    """


class Rectangle:
    """Represents a rectangle.

    attributes: width, height, corner.
    """


#  we instantiate an object named box
box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0


def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p


def print_point(p):
    return 'point (%g, %g)' % (p.x, p.y)


def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight


def print_current_size(rect):
    return rect.width, rect.height


def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy


def move_rectangle_copy(rect, dx, dy):
    """This function creates a copy of the initial
    rectangle and moves it into a new position
    """
    new_rect = copy.deepcopy(rect)
    new_rect.corner.x += dx
    new_rect.corner.y += dy
    return new_rect


current_size = (box.width, box.height)
center_rect = find_center(box)
print('Center of rectangle is', print_point(center_rect))
print('Current size', print_current_size(box))
grow_rectangle(box, 50, 200)
print('Current size', print_current_size(box))
print('Current position', print_point(box.corner))
move_rectangle(box, 5, 10)
print('Current position', print_point(box.corner))

#making a new rectangle in a different position than the initial one
box_2 = move_rectangle_copy(box, 100, 200)
print('New rectangle object position', print_point(box_2.corner))

#  just checking if the 2 objects are the same (value should be false)
print(box_2 is box)
#print(box_2.corner.z)
print(type(box))
print(type(box_2))
print(type(box.corner))
print('Status instance box_2, rectangle',isinstance(box_2, Rectangle))

