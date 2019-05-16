import socket
import time

"""
    This program retrieves an image using HTTP.
    It accumulates the data in a string, trims off the headers,
    and then saves the image data to a file.
    
    Input:
        HOST = 'data.pr4e.org'
        PORT = 80
        Get Request 'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n'

    Output:
        4320 4320
        5120 9440
        [...]
        1008 230608
        Header length 394
        HTTP/1.1 200 OK
        Date: Thu, 16 May 2019 17:19:11 GMT
        Server: Apache/2.4.18 (Ubuntu)
        Last-Modified: Mon, 15 May 2017 12:27:40 GMT
        ETag: "38342-54f8f2e5b6277"
        Accept-Ranges: bytes
        Content-Length: 230210
        Vary: Accept-Encoding
        Cache-Control: max-age=0, no-cache, no-store, must-revalidate
        Pragma: no-cache
        Expires: Wed, 11 Jan 1984 05:00:00 GMT
        Connection: close
        Content-Type: image/jpeg
    Image file is then saved on the local disk
    with the name "stuff.jpg".    
"""

HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b""

while True:
    data = mysock.recv(5120)
    if len(data) < 1:
        break
    time.sleep(0.25)
    count = count + len(data)
    print(len(data), count)
    picture = picture + data

mysock.close()

# Look for the end of the header (2 CRLF)
pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode())

# Skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open("stuff.jpg", "wb")
fhand.write(picture)
fhand.close()

