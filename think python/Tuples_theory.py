t = ('a', 'b', 'c', 'd', 'e') #with or without paranthesis gets to work
print(t)

t1 = 'a', #this is how a single element tuple looks like, you habe to put the final comma
print(t1)

t2 = 'a' #written like that it is a string
print('this a  has type', type(t2))

t3 = ('abc', '123')
print(t3)

t4 = tuple() #this is a built-in function of a tuple, this one creates an empty tuple
print(t4)

t5 = tuple('romania') #this creates a tuple with the elements of the sequence
print(t5)

t6 = ('a', 'b', 'c', 'd', 'plm') #the bracket operator indexes an element
print(t6[0])
print(t6[4])

print(t6[0:3]) #up to but not including :))) the slice operator selects a range of elements

t6 = t6[:4] + ('peleme',)
#dont forget the final comma, you can't modify the elements of a tuple
#but you can replace
#one tuple with another
print(t6)


