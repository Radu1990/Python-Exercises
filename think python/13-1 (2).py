

fin = open('romeo-full.txt')


def print_create_dex(arg):
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


var_1 = print_create_dex(fin)


def print_create_reversed_dictionary(arg):
    dex_reversed = {}
    #  this adds the key, values in reversed order in the new dictionary
    s_dex = []
    #  this sorted dex list is used to print them in descending order
    counter_word_freq = 1
    for x in arg:
        v = arg[x]
        if v not in dex_reversed:
            dex_reversed[v] = x
    for x in dex_reversed:
        s_dex = s_dex + [x]
        s_dex = sorted(s_dex, reverse=True)
    print('Word Frequency as follows: ')
    for x in s_dex[:20]:
        print('Position: ', counter_word_freq, dex_reversed[x])
        counter_word_freq = counter_word_freq + 1


#print_create_reversed_dictionary(var_1)


def choose_from_histogram(t):
    import random
    random_lst = []
    for x in t:
        random_lst = random_lst + [x]

    for i in range(10):
        rand_c = random.choice(random_lst)
        print('"', rand_c, '"', 'with probability', t[rand_c],"/", len(t))


choose_from_histogram(var_1)
