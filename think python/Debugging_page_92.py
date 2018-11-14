# this code checks if one string is identical to the other when spelled backwards (stop pots)

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False  # this acts as guardian if word lengths are different

    i = 0
    j = len(word2)-1

    while j > -1:
        print(i, j)

        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j - 1
    print('True')
    return True

is_reverse('pots', 'stop')




