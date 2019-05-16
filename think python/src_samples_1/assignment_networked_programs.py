import socket

"""
    The program makes a connection to port 80 on the server www.py4e.com.
    The HTTP protocol says we must send the GET command followed by a blank line
    
    Once we send that blank line, we write a loop that receives data in 512-character
    chunks from the socket and prints the data out until there is no more data to read
    
    Output:
        HTTP/1.1 200 OK
        Date: Thu, 16 May 2019 15:04:58 GMT
        Server: Apache/2.4.18 (Ubuntu)
        Last-Modified: Sat, 13 May 2017 11:22:22 GMT
        ETag: "a7-54f6609245537"
        Accept-Ranges: bytes
        Content-Length: 167
        Cache-Control: max-age=0, no-cache, no-store, must-revalidate
        Pragma: no-cache
        Expires: Wed, 11 Jan 1984 05:00:00 GMT
        Connection: close
        Content-Type: text/plain
        
        But soft what light through yonder window breaks
        It is the east and Juliet is the sun
        Arise fair sun and kill the envious moon
        Who is already sick and pale with grief
        
"""

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()
