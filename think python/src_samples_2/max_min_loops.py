#maximum loops
largest = None
print("Before:", largest)
for x in [1, 42, 54, 46, 23, 123, 7, 2, 23, 45, 42]:
    if largest is None or x > largest:
        largest = x
    print("Loop:", x, largest)
print("Largest:", largest)
####minimum loops
smallest = None
print("Before:", smallest)
for x in [42, 54, 46, 23, 123, 7, 2, 23, 45, 42]:
    if smallest is None or x < smallest:
        smallest = x
    print("Loop:", x, smallest)
print("Smallest:", smallest)
