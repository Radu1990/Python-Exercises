# import urllib.request
#
# fhand = urllib.request.urlopen('https://en.wikipedia.org/wiki/Attachment_in_adults')
#
# for line in fhand:
#     print(line.decode().strip())
#
# end

# import urllib.request, urllib.parse, urllib.error
# import re
#
# url = input('Enter - ')
# html = urllib.request.urlopen(url).read()
# links = re.findall(b'href="(http://.*?)"', html)
# for link in links:
#     print(link.decode())
#
# END

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input('Enter- ')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
#
# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     print('TAG:', tag)
#     print('URL:', tag.get('href', None))
#     #print('Contents:', tag.contents[0])
#     print('Attrs:', tag.attrs)
#
# end

# import urllib.request, urllib.parse, urllib.error
#
# import ssl
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# img = urllib.request.urlopen('https://giant.gfycat.com/BareCapitalJabiru.webm').read()
#
# fhand = open('stuff.webm', 'wb')
# fhand.write(img)
# fhand.close()
# #end

