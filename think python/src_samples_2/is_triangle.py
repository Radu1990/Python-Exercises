print('This program checks wether you can form a triangle with 3 different lengths or not')
a = input('a= ')
b = input('b= ')
c = input('c= ')

def is_triangle(a, b, c):
    if a > b + c:
        print ('No')
        return
    if b > a + c:
        print('No')
        return
    if c > a + b:
        print('No')
        return
    else:
        print("Yes")

is_triangle(a,b,c)