def histogram(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c] + 1
            #  c is key in dictionary, and d[key] gets the value

    return d


#print(histogram('brontosaurusmancatias'))

grlgrl = histogram('brontosaurusmancatias')

def reverse_lookup(v, d):

    shopbag = []

    for k in d:

        if d[k] == v:

            print('Key with this value is ', k)

            shopbag = shopbag + [k]



        print('Keys with this value are ', shopbag)

    raise LookupError('no key with that value found brother')


reverse_lookup(2, grlgrl)
