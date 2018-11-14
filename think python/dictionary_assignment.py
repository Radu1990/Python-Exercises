name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
counts = dict()


for line in handle:
    line = line.strip()
    if not line.startswith('From') : continue
    if not line.endswith('2008') : continue
    #print(line)
    list = line.split()
    #print(list)
    try:
        #print(list[1])
        name = list[1]
        #print('Name is ', name)
        if name not in counts:
            counts[name] = 1
        else:
            counts[name] = counts[name] + 1
        #print(counts)
        maximum = max(counts, key=counts.get)
        #print(maximum, counts[maximum])

        ####
    except:
        # print('skip')
        continue
print(maximum, counts[maximum])

#####

