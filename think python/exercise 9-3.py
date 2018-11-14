fin = open('words.txt')  # this opens up the document
forbidden = input('Enter exceptions: ')

count = 0
# number of words which contain no e letter
count_no_forbidden = 0
# number of words containing to forbidden letters
total = 0
# total of words

# this function computes percentage


def compute_percentage(a, b):
    percentage = int(a * 100 / b)

    # where a = number of words which contain no letter
    # where b = total of words

    print('Percentage of words containing no letter e is', percentage, '%')


# this function checks if one letter is found in the specific word


def voids(word, forbidden):
    for x in word:
        print(x)
        if x in forbidden:
            print('False')
            return False
    return True


for line in fin:
    word = line.strip()

    if voids(word, forbidden) is True:
        count_no_forbidden = count_no_forbidden + 1



    if word != 0:
        total = total + 1

    if 'e' not in word:
        count = count + 1

print('Total words', total)
print('No "e" words', count)
print('Words with no forbidden letters', count_no_forbidden)
compute_percentage(count, total)





