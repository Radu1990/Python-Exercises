# Printing the largest number found so far in a loop and the one being currently checked
largest_so_far = -1
print("Before we start looking at the series we know that the largest number so far is: ", largest_so_far)
for the_num in [8, 41, 23, 86, 489, 654, 2 , 51]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print ("Largest number in the series so far is: ", largest_so_far, the_num)

print ("After checking all of the numbers we concluded that the largest number so far is: ", largest_so_far)


#Counting the elements/numbers from a loop
x=0
print("Before starting to check we had", x)
for thing in [4, 54, 123, 42, 3, 28]:
    x=x+1
    print(x, thing)
print("After the series ends we stopped at", x)


# Counting / adding / finding the Average in a Loop"
count = 0
sum = 0
print("Before the count started: ", count, sum)
for value in [9, 41, 12, 3, 75 ,65]:
    count = count+1
    sum = sum + value
    print(count, sum, value)
print("After the countdown ended: ", count, sum, sum / count)

# Filtering in a Loop
print("Before")
for value in [9, 41, 22, 24, 54, 1, 5]:
    if value > 20:
        print("Large number ", value)
print("After")

###Searching Using a Boolean Variable
found = False
print("Before", found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
    if found == True:
        break
print("After", found)
