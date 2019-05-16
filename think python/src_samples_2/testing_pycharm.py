y = None
print("Before:", y)
for x in [42, 54, 46, 23, 123, 7, 2, 23, 45, 42]:
    if y is None or y > x:
        y = x
    print("Loop:", x, y)
print("Smallest:", y)
