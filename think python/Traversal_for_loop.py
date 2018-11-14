prefixes = 'JKLMNOPQ'

suffix = 'ack'

for x in prefixes:
    if x == 'O':
        x = 'Ou'

    elif x == 'Q':
        x = 'Qu'

    print(x + suffix)

fruit = 'banana'

print(fruit[:3])

