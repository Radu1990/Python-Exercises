###search loops using continue

fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    #skip untinteresting line
    if not line.startswith("From:"):
        continue
    ###process our interesting lines:
    print(line)

####search loops using the find string method:

fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if line.find("@uct.ac.za") == -1: continue
    print(line)

