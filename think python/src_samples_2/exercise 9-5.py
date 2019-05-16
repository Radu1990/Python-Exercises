word = input('Type word here: ')
x = len(word)
# x is length of string (-1 comes from string conditions)
y = 0
# y kk,
# word index


def this_func(y, word):

    while y < x-1:

        if word[y] < word[y+1] or word[y] == word[y+1]:
            pass
        else:
            print('Not aabecedarian try again')
            return False

        y = y + 1

    if word[y] > word[y-1] or word[y] == word[y-1]:
        pass
    else:
        print('Not aabecedarian try again')
        return False

    print('Word is aabecedarian!')


this_func(y, word)