import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in fhand:
    print(line.decode().strip())

###

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

counts={}

for line in fhand:
    words=line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

#####
#####

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("http://www.dr-chuck.com/page1.htm")

for line in fhand:
    print(line.decode().strip())
#####
#####

#####beatiful soup
import urllib.request, urllib.parse, urllib.error
from bs4 import beautifulsoup

url = input("Enter - ")
html = urllib.request.urlopen(url).read()
soup = Beautifulsoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup("a")
for tag in tags:
    print(tag.get("href", None))




