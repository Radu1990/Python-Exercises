# this function computes percentage

# this opens up the document
fin = open('words.txt')


def compute_percentage(a, b):
    percentage = int(a * 100 / b)

    # where a = number of words which contain no letter
    # where b = total of words

    print('Percentage of words containing no letter e is', percentage, '%')


count = 0
# number of words which contain no e letter
total = 0
# total of words

for line in fin:
    word = line.strip()
    if word != 0:
        total = total + 1

    if 'e' not in word:
        count = count + 1

print('Total words', total)
print('No "e" words', count)

compute_percentage(count, total)
