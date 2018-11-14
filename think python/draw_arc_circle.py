import turtle

t = turtle.Turtle()

r = input("radius: ") #the smaller the radius, the smaller l should be. if greater then l can be also bigger
rint = int(r)

#l = input("length of segment: ")
#lint = int(l) #the smaller the value of l segment, the smoother the circle will be
#simplifying this
lint = 1

a = input("portion of circle to be drawn: ")
aint = int(a)

pi = 3.14

def square(x, rint, lint, arc): #
    n = ((pi*2*rint)/lint)

    nint = int(n) #this is the number of segments are needed to build a full closed circle

    angle = 360/nint #this angle defines how smooth the circle is drawn derived from 360 degrees divided by n

    single_angle = nint/360
    print("single angle is ", single_angle)

    arc = aint * single_angle
    arcint = int(arc)
    for i in range(arcint):
        x.lt(angle)
        x.fd(lint)

square(t, rint, lint, aint)

