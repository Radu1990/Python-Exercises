print('This program returns True if x <= y <= z')
x=float(input('Type x: '))
y=float(input('Type y: '))
z=float(input('Type z: '))


def is_between(x, y, z):

    if x <= y <= z:
        return True
    else:
        return False


is_between(x, y, z)
print(is_between(x, y, z))

