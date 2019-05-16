# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file


# THIS IS THE LINK WE ARE USING ###
# http://py4e-data.dr-chuck.net/known_by_Ammar.html


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

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


def repeat_process(url_to_use):
    print("Retrieving: ", url_to_use)

    # URLLIB and BEAUTIFULSOUP
    html = urllib.request.urlopen(url_to_use, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    selected_tag = tags[pos_int]

    # TUPLE (URL, NAME)
    return selected_tag.get('href', None), selected_tag.contents[0]


curr_url = url
curr_name = ''
for i in range(1, repeat_times_int + 1):
    url_name_tuple = repeat_process(curr_url)
    curr_url = url_name_tuple[0]
    curr_name = url_name_tuple[1]
    print("curr_url: ", curr_url)
    print("curr_name: ", curr_name)


print("FINAL NAME: ", curr_name)
