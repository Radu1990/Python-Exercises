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
