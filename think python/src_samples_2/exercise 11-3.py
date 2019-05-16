cache = {}
#  this is a memo

def ack(m, n):

    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        result = ack(m-1, 1)
        print(result)
        return result

    elif m > 0 and n > 0:
        cache[m,n] = ack(m-1, ack(m, n-1))
        return cache[m,n]

print (ack(3,4))
#print (ack(3,6))
#print (ack(3,7))
print(cache)
