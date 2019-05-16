hrs = input("Enter Hours please:")
rate_1 = input("Enter rate please:")
#this try and except quits the program if other values are typed in
try:
    h = float(hrs)
    r1 = float(rate_1)
    r2 = float(r1*1.5)
except:
    print("Error")
    quit()
#this def defines a new function that can be later called as a normal function
def computepay():
    otp = ((h-40)*r2)
    otptotal=(40*r1 + otp)
    return otptotal
p=computepay()
print("Hours worked:", h , "Normal rate of pay:", r1, "Overtime rate of pay:", r2 )
normaltimepay = float(h*r1)
if h<=40:
    print("Your wage this month will be:", normaltimepay)
elif h>40:
#this end="" does not allow the print to create a new line after
    print( "Your wage this month will be: ", p )
