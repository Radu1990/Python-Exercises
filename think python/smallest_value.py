smallest_number = None
print ("Before ",smallest_number)
for x in [23, 587, 9, 41, 13, 3, 2, 54, 12, 15, 99]:
    if smallest_number is None: #this runs only once because then it becomes false as smallest_number becomes a value of 23
        smallest_number = x
    #now the code always runs from here as it skips the first line
    elif x < smallest_number:
        smallest_number = x
    print (smallest_number, x)
print("After ", smallest_number)
