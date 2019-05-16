import urllib.request, urllib.error
import xml.etree.ElementTree as elTree

"""
    This program parses an XML file from a specific URL 
    and retrieves the values from the container field
    named "count" and then returns a sum of those values.

    XML file example:
        <commentinfo>
        <note>
        This file contains the actual data for your assignment - good luck!
        </note>
        <comments>
        <comment>
        <name>Allesandro</name>
        <count>100</count>
        </comment>
        [...]
        
    Input: 
        Enter location: http://py4e-data.dr-chuck.net/comments_101605.xml

    Output:    
        Retrieving http://py4e-data.dr-chuck.net/comments_101605.xml
        count value is  100
        sum is 100
        count value is  98
        sum is 198
        [...]
"""

while True:
    address = input('Enter location: ')
    if address == "done":
        address = "http://py4e-data.dr-chuck.net/comments_101605.xml"
    elif len(address) < 1:
        break

    url = address
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    tree = elTree.fromstring(data)

    counts = tree.findall('comments/comment')

    sum = 0

    for item in counts:
        count_int = int(item.find("count").text)
        print("count value is ", count_int)
        sum = sum + count_int
        print("sum is", sum)
