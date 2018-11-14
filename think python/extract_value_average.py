# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total_conf = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue #this skips (continues) all the lines that dont start with that
    count = count + 1
    print('Count is ', count)
    #print(line.rstrip())
    var_a = line.find(':')
    confnumber = line[var_a + 1:].strip()
    confnumber = float(confnumber)
    print('Confidence number is', confnumber)
    total_conf = total_conf + confnumber
    print('total is', total_conf)
average_conf = total_conf / count
print('The average conf is:', average_conf)


print("Done")
