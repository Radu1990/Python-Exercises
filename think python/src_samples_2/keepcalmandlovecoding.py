#  write a function that takes multiple arguments


def sumall(*args):

    lst_args = []
    counter_sum = 0
    item_nr = 0

    for x in args:
        lst_args = lst_args + [x]
    print('Variable length argument is ', lst_args)

    for element in lst_args:

        counter_sum = counter_sum + element
        item_nr = item_nr + 1
    print('SUM IS: ', counter_sum)


sumall(1,2,3,123,42,7546)

