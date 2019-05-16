# the purpose of this exercise is to check
# how every individual function works!

s = 'aaabaaba'


def any_lowercase1(s):
    for c in s:
        # we call the function c.islower() and check if it is true or false (will check only first letter)
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    for c in s:
        if c.islower():  # this functions verifies if the string 'c' is a lowercase letter
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    for c in s:
        flag = c.islower()
        # we put the function c.islower() in a variable named flag
        # then we call it for every letter c of the string s
    return flag
# then we return the last result of the flag function (True or False)


def any_lowercase4(s):
    flag = False  # we attribute a boolean False to the variable flag
    for c in s:
        flag = flag or c.islower()
        # flag variable gets to be replaced by flag value which is at first False or by c.islower()of each letter c in s
        # in any case if one of the letters is a lower case letter then the condition turns to True
        # and is overwritten everywhere further because True is chosen over False
        print(flag)
    return flag


def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

# this function proves if c in s is NOT a lower case letter(so an UPPER CASE LETTER) then returns False
# if it reaches the end and all are LOWERCASE LETTERS it returns TRUE


print(any_lowercase5(s))
