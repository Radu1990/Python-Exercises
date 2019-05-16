import turtle

"""
    This program uses turtle.py: a Tkinter based turtle graphics module for Python
    This program draws a circle using input as circle radius and circle circumference
"""

t = turtle.Turtle()
pi = 3.14

# the smaller the radius, the smaller l should be

r = input("radius: ")
rint = int(r)

# l = length of segment
l = 1
# a = portion of circle to be drawn
a = input("portion of circle to be drawn: ")
aint = int(a)


def square(x, rint, lint, arc):
    n = ((pi*2*rint)/lint)

    # this is the number of segments are needed to build a full closed circle
    nint = int(n)

    # this angle defines how smooth the circle is drawn derived from 360 degrees divided by n
    angle = 360/nint

    single_angle = nint/360
    print("single angle is ", single_angle)

    arc = aint * single_angle
    arcint = int(arc)

    for i in range(arcint):
        x.lt(angle)
        x.fd(lint)


square(t, rint, l, aint)
