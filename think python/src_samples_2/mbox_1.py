####\n

word="Hello\nWorld"
print(word)

####reading files

fhandle = open("mbox-short.txt")
count = 0
for line in fhandle:
    count = count +1
print("Count in mbox short=", count)

##### reading file and displaying number of characters inside the file and printing the first words from a line

fhand = open("mbox-short.txt")
inp = fhand.read()
print(len(inp))
print(inp[:50])
quit()

####searching through a file for some lines containting words ( works in a separate file)

fvar = open("mbox-short.txt")
for line in fvar:
    if line.startswith("From: "):
        print(line)

###### ( works in a separate file)

fhand=open("mbox-short.txt")

for line in fhand:
    line=line.rstrip()
    if line.startswith('From:'):
        print(line)
