#defining one simple function
def print_lyrics():
    print ("You better lose yourself in the music, the moment")
    print ("You own it, you better never let it go")
    print ("You only get one shot, do not miss your chance to blow")
    print ("This opportunity comes once in a lifetime")
#defining another function using the function before
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
print_lyrics()
repeat_lyrics()
###
print ()
inp=input("Enter the value you want printed twice: ")
def print_twice(inp):
    print(inp)
    print(inp)
print_twice(inp)
