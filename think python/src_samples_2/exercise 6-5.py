
print('This program calculates the greatest common divisor with Euclid algorithm')

a = int(input('a='))
b = int(input('b='))


def gcd(a, b):
    # catch base case from the door
    if b == 0:
        return a
    # otherwise, do the other steps
    else:
        remainder = a % b  # compute remainder
    # If we have base case,
    # no need to call again
    if remainder == 0:
        return b
    # otherwise, we recurse and grab the return value
    else:
        return gcd(b, remainder)


print(gcd(a,b))

# Printing only 'y' which is the GCD between a and b




