# find a word with 3 consecutive double letters

fin = open('words.txt')  # this opens up the document

line = fin.readline()

def check_line(input):
    x = 0 # word index

    word = input.strip()

    j = len(word)  # length of word

    if j < 6:

        return False

    while x < j:
        try:

            if word[x] == word[x+1] and word[x+2] == word[x+3] and word[x+4] == word[x+5]:
                print('Word is a match! Word is: ', word)
                return True
            x = x + 1

        except:
            return False


for line in fin:

    check_line(line)


# this is a better solution...
#def is_triple_double(word):
#    """Tests if a word contains three consecutive double letters.
#
#    word: string
#
#    returns: bool
#    """
#    i = 0
#    count = 0
#    while i < len(word) - 1:
#        if word[i] == word[i + 1]:
#            count = count + 1
#            if count == 3:
#                return True
#            i = i + 2
#        else:
#            count = 0
#            i = i + 1
#    return False














