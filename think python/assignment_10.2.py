
######################################################
#                                                    #
# Thank you Charles for the wonderful course so far! #
#                                                    #
######################################################

name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    line = line.strip()
    if not line.startswith('From') : continue
    if not line.endswith('2008') : continue

    list_0 = line.split() #here we break the line in words
    time = list_0[5] #here we select the time from the sequence where time is the 5th element
    time = list_0[5].split(":") #here we break the time string using the : symbol into more pieces
    hour = time[0] #here we assign to hour variable the first piece from the sequence above which is the hour

    if hour not in counts:
        counts[hour] = 1
    else:
        counts[hour] += 1 #here we create a dictionary where we create a list of hours in the dictionary using keys as hours and incrementing values

    list_1 = list(counts.items()) #here we create a new list where we bring all the elements (key-value) from the dictionary
    list_1.sort() #here we sort the list after the keys

for key, value in list_1:
    print(key, value) #in the end we choose to print the key, values from the sorted list
