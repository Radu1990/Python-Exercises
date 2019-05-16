score = input("Enter score:")

s = float(score)

if s < 0.0 or s > 1.0:
    print("This value is not allowed.")
else:
    if s >= 0.9:
        print("A")
    elif s >= 0.8 and s < 0.9:
        print("B")
    elif s >= 0.7 and s < 0.8:
        print("C")
    elif s >=  0.6 and s < 0.7:
        print("D")
    elif s < 0.6:
        print("F")
