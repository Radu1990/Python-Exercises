def do_twice(f, val):
    f(val)
    f(val)


def print_shit(x):
    print(x)

def print_twice(bruce):
    print(bruce)
    print(bruce)

#do_twice(print_twice, "spam")

def do_four(func, arg):
    """Runs a function four times.

    func: function object
    arg: argument passed to the function
    """
    do_twice(func, arg)
    do_twice(func, arg)
do_four(print_shit, 'Gran Canaria')

