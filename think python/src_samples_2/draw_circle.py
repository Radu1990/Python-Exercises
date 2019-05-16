import turtle

t = turtle.Turtle()

r = input("radius: ")
rint = int(r)

l = input("length of segment: ")
lint = int(l)

pi = 3.1415926


def square(x, rint, lint):
    n = ((pi*2*rint)/lint)
    nint = int(n)
    angle = 360/nint

    for i in range(nint):
        x.lt(angle)
        x.fd(lint)


square(t, rint, lint)
