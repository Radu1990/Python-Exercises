#  this function takes a list and return True if there is any element that appears more than once.
#  it should not modify the list

t8 = [1, 2, 3, 4, 5, 6, 4, 7, 4, 8, 9, 10]

new_dict = {}
counter = 0


def has_duplicates(input_list):
    for x in input_list:
        if x in new_dict:
            print('Duplicate', x, 'detected, aborting mission...')
            return True
        new_dict[x] = True
        print(new_dict)
    print('No duplicates detected')
    return False


print(has_duplicates(t8))