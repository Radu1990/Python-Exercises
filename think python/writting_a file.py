#to write a file you have to open with w a second parameter
fout = open('letswrite.txt', 'w')
print(fout)
line_0 = 'This is our first attempt to write something in a file using Python'
fout.write(line_0)
line_1 = '000'
fout.write(line_1)
line_2 = '\nNow we start to write using the new line character'
fout.write(line_2)