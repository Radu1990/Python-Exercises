import urllib.request, urllib.parse, urllib.error
import json

sum = 0
count = 0

address = input("Enter location: ") #http://py4e-data.dr-chuck.net/comments_101606.json
url = address
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None
#if not js or 'status' not in js or js['status'] != 'OK':
    #print('=====Failure to retrieve data=====')
    #print(data)

#print(js)
lst = js['comments']
for item in lst:
    #print('Name', item['name'])
    #print('Comment counts', item['count'])
    variable_sum = item['count']
    count = count + 1
    sum = sum + variable_sum
    #print('sum is ', sum)
print('Count is: ', count)
print('Sum is: ', sum)