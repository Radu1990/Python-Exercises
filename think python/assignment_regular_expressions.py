import re
filehandle = open("regex_sum_101601.txt")
sum = 0
for line in filehandle:
    line = line.strip()
    x = re.findall("[0-9]+", line)
    if len(x) > 0:
        print(x)
    for number in x:
        y=float(number)
        print(y)
        sum = sum + y
        print(sum)