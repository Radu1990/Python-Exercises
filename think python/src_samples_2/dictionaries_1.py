def histogram(s):
    d = {}
    for c in s:

        count = d.get(c, 0)

        d[c] = count + 1

    print(d)

    return d


histogram('aaaaabc')