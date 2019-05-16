
"""
Docstring:
In order to use this function, n always has to have positive values, otherwise you get an infinite recursion.
"""


def recurse(n,s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

