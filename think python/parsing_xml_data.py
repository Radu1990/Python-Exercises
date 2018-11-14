import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

while True:
    address = input('Enter location: ')
    if address == "done":
       address = ("http://py4e-data.dr-chuck.net/comments_101605.xml")
    elif len(address) < 1: break

    url = address
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    #print('Retrieved', len(data), 'characters')
    #print(data.decode())
    tree = ET.fromstring(data)

    counts = tree.findall('comments/comment')

    sum = 0

    for item in counts:
        count_int = int(item.find("count").text)
        print("count value is ", count_int)
        sum = sum + count_int
        print("sum is", sum)
###########################################
##############               ##############
############## T H E   E N D ##############
##############               ##############
###########################################
