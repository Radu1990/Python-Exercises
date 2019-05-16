fin = open('words.txt')

searched_word = input('What you want to look for?  >')

words_lst = []
counter = 0

for line in fin:

    word = line.strip()

    words_lst = words_lst + [word]

    counter = counter + 1

    if counter == 1000:
        break

sorted_lst = sorted(words_lst)

print(sorted_lst)


def in_bisect(x, y):
    #  x is sorted list
    #  y is target value
    try:
        print('Index of ', searched_word, 'is', x.index(y))
        return x.index(y)
    except:
        print(y, 'is not in list')
        return None


in_bisect(sorted_lst, searched_word)