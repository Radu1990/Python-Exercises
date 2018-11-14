import turtle
t = turtle.Turtle()

def koch(t, n):
    '''Draws a Koch curve with length n'''
    if n<10:
        t.fd(n)
        return
    m = n / 3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)
#koch(t, 300)

def snowflake(t, n):
    '''Draws a snowflake (a triangle with a Koch curve for each side.'''
    for i in range(3):
        koch(t, n)
        t.rt

t.pu()
t.goto(-150, 90)
t.pd()
snowflake(t, 300)