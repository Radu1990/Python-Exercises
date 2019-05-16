import turtle

bob = turtle.Turtle()

nsides = input("Enter number of sides: ")
# creating an integer out of number of sides input
nint = int(nsides)


# defining function with number
# of sides, length as input
def square(x, nint, length):
    angle = 360/nint
    for i in range(nint):
        x.lt(angle)
        x.fd(length)


square(bob, nint, 100)
