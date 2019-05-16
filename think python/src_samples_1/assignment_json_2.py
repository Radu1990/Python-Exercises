import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
# for this API

"""
    The program takes the search string and constructs a URL with the search string
    as a properly encoded parameter and then uses urllib to retrieve the text from
    the Google geocoding API. Unlike a fixed web page, the data we get depends on the
    parameters we send and the geographical data stored in Google's servers.

    Once we retrieve the JSON data, we parse it with the json library and do a few
    checks to make sure that we received good data, then extract the information that
    we are looking for.
    
    Input:
        Polytechnic University of Timisoara
    Output:
        Retrieving http://py4e-data.dr-chuck.net/geojson?address=Polytechnic+University+of+Timisoara
        Retrieved 1750 characters
        {
            "results": [
                {
                    "address_components": [
                        {
                            "long_name": "Timi\u0219oara",
                            "short_name": "Timi\u0219oara",
                            "types": [
                                "locality",
                                "political"
                           ...
            ],
            "status": "OK"
        }
        lat 45.7488716 lng 21.2086793
        Timișoara, Romania
"""


serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    url = serviceurl + urllib.parse.urlencode(
        {'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
