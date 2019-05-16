import string

fhand = open('romeo-full.txt')

counts = dict()

for line in fhand:
    # this removes all the punctuation
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            # this translates as: for "word" variable in words sequence,
            # if word is not in dictionary, assign value 1 to the word,
            # otherwise, increment 1
            counts[word] = 1
        else:
            counts[word] += 1

# Sort the dictionary by value
lst = list()
# we get all the items of counts inside list()
for k, v in list(counts.items()):
    # we construct a list of v, k tuples and sort it in reverse order
    lst.append((v, k))
    lst.sort(reverse=True)
    # here we list the first 10 words
for k, v in lst[:10]:
    print(k, v)
