####Parsing and Extracting
####From elon.musk@tesla.com Sat Jan 5 09:14:16 2008

data = "From elon.musk@tesla.com Sat Jan 5 09:14:16 2008"
atpos = data.find("@")
spacepos= data.find(" ",atpos) #this atpos second argument gives the line from where it should start to search
emailhost=data[atpos+1 : spacepos]
print("The data you were trying to search is:", emailhost)
###assignment 6.5
text = "X-DSPAM-Confidence:    0.8475";
numberpos = text.find("0")
numberdisplay = text[numberpos : ]
fnum = float(numberdisplay)
print(fnum)
#####better alternative
text = "X-DSPAM-Confidence:    0.8475"
ipos = text.find(":")
numbervar = text[ipos+1 : ]
print(numbervar)
value = float(numbervar)
print(value)

