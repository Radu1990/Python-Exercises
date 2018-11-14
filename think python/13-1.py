fin = open('romeo-full.txt')


def print_split_in_words(arg):
    counter = 0
    dex = {}
    for line in arg:
        words = line.strip().split()

        for word in words:
            counter = counter + 1

            if word not in dex:
                dex[word] = 0

            else:
                dex[word] = dex[word] + 1
    print('Total words:', counter)
    return dex

var_1 = print_split_in_words(fin)

def print_create_reversed_dictionary(arg):
    dex_reversed = {}
    s_dex = []
    for x in arg:
        v = arg[x]
        if v not in dex_reversed:
            dex_reversed[v] = x
    for x in dex_reversed:
        s_dex = s_dex + [x]
    s_dex_ordered = sorted(s_dex, reverse=True)
    for x in s_dex_ordered:
        print('Word Frequency: ', x, dex_reversed[x])

print_create_reversed_dictionary(var_1)
