def invert_dict(d):
    inverse = {}
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = key
        else:
            inverse[val].append(key)
    return inverse


d = {'one': 'unu', 'two': 'doi', 'three': 'trei'}


print(d)
inv_dict = invert_dict(d)
print(inv_dict)

print(d['one'])