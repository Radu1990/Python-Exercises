def right_justify(s):

    space = ('-')  # one slot of free space string
    tofill = (70-len(s))  # amount of space to be filled
    output = (space*tofill+s)  # this is the expression that displays
    print('Space to be filled: ', tofill)
    print(output)


right_justify("Rick and Morty")
