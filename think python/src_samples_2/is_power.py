a = input('Type a value: ')
b = input('Type b value: ')

def is_power(a, b):

    if a % b == 0 and ((a / b) % 2) == 0 :
        return True
    else:
        return False
print('This program verifies if "a" is a power of "b" in base 2')
print(is_power(8,2))
