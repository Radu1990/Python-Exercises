import urllib.request, urllib.error
import json

"""
    This program parses a JSON file from a specific URL 
    and retrieves the values from the container field
    named "count" and then returns a sum of those values.
    
    Json file example:
            {
      "note":"This file contains the actual data for your assignment",
      "comments":[
        {
          "name":"Kainui",
          "count":99
        },
        [...]
             }   
    
    Input: 
        Enter location: http://py4e-data.dr-chuck.net/comments_101606.json 
    
    Output:    
        Retrieving http://py4e-data.dr-chuck.net/comments_101606.json 
        Retrieved 2734 characters
        Count is:  50
        Sum is:  2903
"""

sum = 0
count = 0

# http://py4e-data.dr-chuck.net/comments_101606.json
address = input("Enter location: ")
url = address
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

lst = js['comments']
for item in lst:

    variable_sum = item['count']
    count = count + 1
    sum = sum + variable_sum

print('Count is: ', count)
print('Sum is: ', sum)
