name = input("Enter file:")

if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)
counts = {}


def max_value(email_to_occurrences):
    max_occurrences = 0
    max_email = ''

    for curr_key, curr_val in email_to_occurrences.items():
        if curr_val > max_occurrences:
            max_occurrences = curr_val
            max_email = curr_key

    print('{0} {1}'.format(max_email, max_occurrences))


for line in handle:
    line = line.strip()
    if not line.startswith('From'):
        continue
    if not line.endswith('2008'):
        continue
    split_line = line.split()
    try:
        name = split_line[1]
        if name not in counts:
            counts[name] = 1
        else:
            counts[name] = counts[name] + 1
    except:
        # print('skip')
        continue

#print(counts)

max_value(counts)
