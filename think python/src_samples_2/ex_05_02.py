smallest = None
largest = None

while True:
    inp = input("Enter some numbers and type done when you are finished: ")
    if inp == "done":
        break
    try:
        int_inp = int(inp)
    except:
        print("Invalid input")
        continue

# smallest number conditioning loop
    if smallest is None:
        smallest = int_inp
    if smallest > int_inp:
        smallest = int_inp

# largest number conditioning loop
    if largest is None:
        largest = int_inp
    if largest < int_inp:
        largest = int_inp

print("Maximum is", largest)
print("Minimum is", smallest)
