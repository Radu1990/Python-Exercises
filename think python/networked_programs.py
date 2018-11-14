##retrieving text##
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org", 80))
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode(), end="")

mysock.close()
#####
#####
##3retrieving an image
import socket
import time

HOST = "data.pr4e.org"
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b"GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n")
count = 0
picture = b""

while True:
    data = mysock.recv(5120)
    if (len(data) < 1): break
    #time.sleep(0.25)
    count = count + len(data)
    print(len(data), count)
    picture = picture + data

mysock.close()

# look for the end of the header (2 CRLF)
pos = picture.find(b"\r\n\r\n")
print("Header length", pos)
print(picture[:pos].decode())

# skip past the header and save the picture data
picture = picture[pos + 4:]
fhand = open("stuff.jpg", "wb")
fhand.write(picture)
fhand.close()




