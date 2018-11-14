fin = open('words.txt')

d = {}


def read_add_dict(arg_input):

    for line in arg_input:
        word = line.strip()

        if word not in d:

            d[word] = 1

        else:

            d[word] = d[word] + 1

    print(d)
    return d


#  read_add_dict(fin)


def check_word(arg_input):

    if arg_input in d:

        print('Word found: ', arg_input)
        return True

    else:

        print('Word not found')
        return False


#  check_word('handicap')


