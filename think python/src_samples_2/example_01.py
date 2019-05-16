# here is an example of a loop that
# copies its input until the user types "Done"
# but treats lines that start with # as lines
# not to be printed

while True:
    line = input(">")
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)
print("Done!")
