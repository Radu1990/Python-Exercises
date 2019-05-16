'''
#recursion
s = int(input('Enter value for s = '))
n = int(input('Enter value for n = '))

def print_n(s,n):
    if n <=0:
        return
    print(s)
    print_n(s, n-1)

print_n(s,n)
'''

#iteration with a while loop
s = int(input('Enter value for s = '))
n = int(input('Enter value for n = '))
def print_n(s, n):
    while n > 0:
        print(s)
        n = n-1
    return

print_n(s,n)