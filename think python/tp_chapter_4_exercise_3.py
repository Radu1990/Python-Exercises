import turtle

bob = turtle.Turtle()

nsides = input("Enter number of sides: ")
nint = int(nsides) #creating an integer out of number of sides input

def square(x, nint , length): #defining function with number of sides, length as input

    angle = 360/nint

    for i in range(nint):
        x.lt(angle)
        x.fd(length)


square(bob, nint, 100)