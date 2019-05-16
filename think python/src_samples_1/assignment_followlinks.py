import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

"""
    This program opens an URL, retrieves all of the anchor tags,
    and returns the desired url from the position entered.

    While following that specific link it then repeats the process as
    many times as desired, retrieving the nth url every time to the user.

    Input:
        target URL: http://py4e-data.dr-chuck.net/known_by_Ammar.html
        Enter position: 1
        Repeat process so many times: 3

    Output:
        Retrieving:  http://py4e-data.dr-chuck.net/known_by_Eng.html
        Retrieving:  http://py4e-data.dr-chuck.net/known_by_Bowie.html
        Retrieving:  http://py4e-data.dr-chuck.net/known_by_Gianmarco.html
"""

# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file


# THIS IS THE LINK WE ARE USING ###
# http://py4e-data.dr-chuck.net/known_by_Ammar.html

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Declare inputs
# url = input('Enter URL: ')
url = "http://py4e-data.dr-chuck.net/known_by_Ammar.html"
pos = input("Enter position: ")
pos_int = (int(pos) - 1)
repeat_times = input("Repeat process so many times: ")
repeat_times_int = int(repeat_times)


def repeat_process():
    # URLLIB and BEAUTIFULSOUP
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    count = 0
    d = dict()

    for tag in tags:
        urlvar = tag.get('href', None)
        cont_var = tag.contents[0]

        if cont_var is not None:
            count = count + 1
            d[urlvar] = count

    # list of all the links
    lst = list(d.keys())
    x = lst[pos_int]
    return x


n = repeat_times_int

while n > 0:
    repeat_process()
    new_url = repeat_process()
    url = new_url
    n = n - 1
    print("Retrieving: ", new_url)
