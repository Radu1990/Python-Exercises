fname = input('Enter file name')
if len(fname) < 1:
    fname = 'clown.txt'
hand = open(fname)

dict = {}
for line in hand:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        dict[w] = dict.get(w,0) + 1

# now we want to find the most common word

largest = -1
theword = None

for k, v in dict.items():
    print(k, v)
    if v > largest:
        largest = v
        theword = k  # capture/remember the word that was largest
print('largest value is', "''", theword, largest, "''")
