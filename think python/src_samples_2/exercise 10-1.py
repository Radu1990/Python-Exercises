t1 = [[1, 2], [3], [4, 5, 6]]
t2 = [1, 2, 3]
t3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t4 = [0, 1, 2, 5, 4, 3, 2, 1]
t5 = 'dog'
t6 = 'god'
t7 = 'doggo'
t8 = [1, 2, 3, 4, 5, 6, 4, 7, 8, 9, 10]


#  nested sum computes the sum of all elements in the nested lists and returns a total
def nested_sum(list):

    sum_of_all = 0
    #  we initialize the variable

    for x in list:
        for x in x:
            print(x)
            sum_of_all = sum_of_all + x
    print(sum_of_all)
    return sum_of_all


#  nested_sum(t1)
#  function cumsum() returns a new list where each element is the sum of the previous elements and the next element
#  example [1,2,3] --- [1, 1+2, 1+2+3, ..., 1+2+...+n]
#  result for [1,2,3] = [1,3,6]
def cumsum(list):

    x = 0
    #  index of list elements:

    e_sum = 0
    #  elements of cumulative sum

    total_e_sum = 0
    #  the sum of the elements

    r_sum = len(list)

    new_list = []

    for element in range(r_sum):
        print('range is', range(r_sum))
        print('element is', element)

        e_sum = e_sum + list[x]

        total_e_sum = total_e_sum + e_sum

        x = x + 1
        print('e_sum is', e_sum)
        print('total sum is', total_e_sum)

        new_list = new_list + [e_sum]

    print('The new list is: ', new_list)


#  cumsum(t2)
#  this function returns a list containing all but the first and the last elements from a list
def middle(list):
    middle_list = list[1:-1]
    return(middle_list)


#  middle(t3)
#  this function modifies the list and returns None
#  if you print the initial list you get the modified version of the list
def chop(t_list):

    del t_list[0]
    del t_list[-1]


#  chop(t3)
#  print(t3)
# this function returns true if list is sorted in ascendant mode
def is_sorted(t_list):

    new_sorted_list = sorted(t_list)

    if new_sorted_list == t_list:
        print('True! Elements are in ascending order')
        return True
    else:
        print('False! Elements are not in ascending order')
        return False


#  is_sorted(t3)
#  this function takes two strings and proves if they are anagrams
def is_anagram(string1, string2):

    # first and foremost we check if both strings have the same number of letters :)
    if len(string1) != len(string2):
        print('Words may have the same letter composition but one word is longer than the other')
        return False
    for letter in string1:
        if letter not in string2:
            print('Not Anagram')
            return False
    #  second we check if all letters in string 1 are found in string 2
    for letter in string2:
        if letter not in string1:
            print('Not Anagram')
            return False
    #  lastly we check if all letters in string 2 are found in string 1 (if string 2 is longer than string 1)
    print('Should be ANAGRAM!')
    return True
    #  we return True otherwise


#  is_anagram(t5,t7)
#  this function takes a list and return True if there is any element that appears more than once.
#  it should not modify the list
def has_duplicates(input_list):
    filtered_list = []
    for x in input_list:
        if x not in filtered_list:
            filtered_list = filtered_list + [x]
        else:
            print('Duplicate detected...duplicate is:', x)
    print('The filtered list is:', filtered_list)
    return True
#  has_duplicates(t8)


