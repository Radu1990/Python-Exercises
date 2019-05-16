def ack(m, n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        result = ack(m-1, 1)
        print(result)
        return result
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))


ack(5, 7)
print(ack(5, 7))
