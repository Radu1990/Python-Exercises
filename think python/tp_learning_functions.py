def hello_world():
    print('Hello World')

def goodbye_world():
    print('Gooby Pls')


def do_n(f, n):
    print(f, n)
    if n <= 0:
        return
    f()
    do_n(f, n-1)

do_n(hello_world, 3)
do_n(goodbye_world, 3)