import turtle

t = turtle.Turtle()

# the smaller the radius, the smaller l should be.
# if greater then l can be also bigger
r = input("radius: ")
rint = int(r)

# l = input("length of segment: ")
lint = 1

a = input("portion of circle to be drawn: ")
aint = int(a)
pi = 3.14


def square(x, rint, lint):
    n = ((pi*2*rint)/lint)
    # this is the number of segments
    # are needed to build a full closed circle
    nint = int(n)
    # this angle defines how smooth the circle
    # is drawn derived from 360 degrees divided by n
    angle = 360/nint
    single_angle = nint/360
    print("single angle is ", single_angle)
    arc = aint * single_angle
    arcint = int(arc)
    for i in range(arcint):
        x.lt(angle)
        x.fd(lint)


square(t, rint, lint, aint)
