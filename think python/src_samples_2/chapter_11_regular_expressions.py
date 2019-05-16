#Matching and extracting data
import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
z = re.findall('[AEIOM]+',x)
print(y)
print(z)
hand = open("mbox-short.txt")
#search for lines that contain "From"
for line in hand:
    line = line.rstrip()
    if re.search("From:", line):
        print(line)
#search for lines that start with From
for line in hand:
    line = line.rstrip()
    if re.search("^From:", line):
        print(line)
#search for lines that start with F , followed by 2 characters, folowed by "m:"
for line in hand:
    line = line.rstrip()
    if re.search("^F..m:", line):
        print(line)
#seach for lines that start with From  and have an @ sign
for line in hand:
    line = line.rstrip()
    if re.search("^From:.+@", line):
        print(line)
s = "A message from csev@yahoo.com to john@mirc.ro about meeting @2pm"
lst = re.findall("\S+@\S+", s)
print(lst)
####
#search for lines that have an at sign between characters
for line in hand:
    line = line.rstrip()
    x = re.findall("\S+@\S+")
    if len(x) > 0:
        print(x)
#######
######
#search for lines that have an at sign between characters
#the characters must be a letter or number
import re
hand = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()
    x = re.findall("[a-zA-Z0-9]\S+@\S+[a-zA-Z]", line)
    if len(x) > 0:
        print(x)
#search for lines that start with "X" followed by any non whitespace characters and ":" followed by a space and any number or a period.(a decimal too)
import re
hand = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if re.search("^X\S*: [0-9.]", line):
        print (line)
#search for lines that start with "X" followed by any non whitespace characters and ":" followed by a space and any number or a period.(a decimal too) then print the number if it is greater than zero
import re
hand = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()
    x = re.findall("^X\S*: ([0-9.]+)", line)
    if len(x) > 0:
        print(x)
#Search for lines that start with "Details: rev=" followed by numbers and "." then print the number if it is greater than 0
import re
hand = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()
    x = re.findall("Details:.*rev=([0-9.]+)", line)
    if len(x) > 0:
        print(x)
#Serach for line that start with From and a character followed by a two digit number between 00 and 99 followed by ":"
#Then print the number if it is greater than zero
import re
hand = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()
    x = re.findall("^From .* ([0-9][0-9]):", line)
    if len(x) > 0: print(x)
####symbols
import re
x = "We just received $10.00 for cookies."
y = re.findall("\$[0-9.]+", x)
print(y)



