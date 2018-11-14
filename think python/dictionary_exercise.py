fname = input('Enter file name')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

dict = {}
for line in hand:
    line = line.rstrip()
    #print(line)
    wds = line.split()
    #print(wds)
    for w in wds:
        # if the key is not there, the count is zero
        #oldcount = dict.get(w,0)
        #print(w, 'old value', oldcount)
        #newcount = oldcount + 1
        #print(w, 'new value', newcount)
        #dict[w] = newcount
        #####################################
        #idiom: retrieve / create / update counter
        dict[w] = dict.get(w,0) + 1
        #print(w, 'new', dict[w])

#print(dict)

#now we want to find the most common word


largest = -1
theword = None

for k,v in dict.items() :
    print (k,v)
    if v > largest:
        largest = v
        theword = k #capture/remember the word that was largest
print ('largest value is',"''" ,theword, largest, "''")