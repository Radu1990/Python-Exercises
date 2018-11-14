d = {'one': 1, 'two': 2, 'three': 3, 'fuckinpieceofcrap': 3, 'aaabc': 3}

#  Inverts a dictionary, returning a map from val to a list of keys.
#
#     If the mapping key->val appears in d, then in the new dictionary
#     val maps to a list that includes key.

def invert_dict(d):
    inverse = {}
    for key in d:
        print(key)
        val = d[key]
        print(val)
        inverse.setdefault(val, []).append(key)
        print('___', inverse)
    print(inverse)
    return inverse

invert_dict(d)

