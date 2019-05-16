from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

"""
    This program retrieves a html document, parses the html document
    and retrieves all the anchor tags named "span", and prints out the
    values contained in the "span class" while summing them as-well.
    
    Input:
        http://py4e-data.dr-chuck.net/comments_42.html
    Ouput:
        Contents: 97
        97.0
        Contents: 97
        194.0
        [...]
        Contents: 2
        2553.0
                        
"""

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL(followed by a blank space): ')
#http://py4e-data.dr-chuck.net/comments_42.html
#http://py4e-data.dr-chuck.net/comments_101603.html

html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
print(tags)

sum = 0
for tag in tags:
    # Look at the parts of a tag
    print('Contents:', tag.contents[0])
    floaty_content = float(tag.contents[0])
    sum = sum + floaty_content

    print(sum)


