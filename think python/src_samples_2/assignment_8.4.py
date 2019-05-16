fname = input('Enter file name: ')
fh = open(fname)
lst = list()
for line in fh:
    #print(line.strip())
    linesplit = line.split()
    #print(linesplit)
    #word will be the traverse
    for word in linesplit:
        if word not in lst:
            lst.append(word)
            #print(lst)
        else: continue
lst.sort()
print(lst)
