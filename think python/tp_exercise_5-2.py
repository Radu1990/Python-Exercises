print("Fermat's Last Theorem: there is no a**n + b**n = c**n for n greater than 2")
a = input('Enter value a: ')
b = input('Enter value b: ')
c = input('Enter value c: ')
n = input('Enter value n: ')

a = int(a)
b = int(b)
c = int(c)
n = int(n)

x = (a**n) + (b**n)
y = (c**n)

if n > 2:
    if x == y:
        print('Holy shit! Fermat got pawned!')
    if x != y:
        print('Values are not the same, Fermat was not a liar')
        print('X is ', x, 'Y is ', y)
elif n <= 2:
    print('n should be greater than 2')