def do_twice(f, val):
    f(val)
    f(val)


def print_this(x):
    print(x)


def print_twice(bruce):
    print(bruce)
    print(bruce)


def do_four(func, arg):
    """Runs a function four times.

    func: function object
    arg: argument passed to the function
    """
    do_twice(func, arg)
    do_twice(func, arg)


do_four(print_this, 'Gran Canaria')

