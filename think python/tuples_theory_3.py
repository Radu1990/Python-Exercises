import string
fhand = open('romeo-full.txt')
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation)) #i think this removes all the punctuation
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1 #this translates as: for "word" variable in words sequence, if word is not in dictionary, assign value 1 to the word, otherwise, increment 1
        else:
            counts[word] += 1

#Sort the dictionary by value

lst = list()
for k, v in list(counts.items()):#we get all the items of counts inside list()
    lst.append((v, k)) #we construct a list of v, k tuples and sort it in reverse order
    lst.sort(reverse=True)
for k,v in lst[:10]:  #here we list the first 10 words
    print(k,v)





