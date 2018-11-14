import turtle

bob = turtle.Turtle()

def square(x, angle, length):

    for i in range(4):
        x.lt(angle)
        x.fd(length)


square(bob, 90, 200)