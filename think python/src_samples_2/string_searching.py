
def find(word, letter, letterfrom):
    # letterfrom is a third parameter
    # which indicates the index where it should start looking from
    index = letterfrom
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


print('The index you are looking for is: ', find('loopingandcounting', 'g', 10 ))
