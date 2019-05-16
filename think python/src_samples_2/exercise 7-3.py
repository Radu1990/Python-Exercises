
# Numerical aproximation of 1/pi

import math


def first_computation():
    x = (2 * math.sqrt(2)) / 9801
    print('First computation equals to', x)
    print('\t')
    return x


def series_computation():
    k = 0
    last_result_sum = 1e-15  # this value is reference for breaking point
    total_sum = 0
    while True:
        result_sum = ((math.factorial(4 * k)) * (1103 + 26390 * k)) / (((math.factorial(k)) ** 4) * (396 ** (4 * k)))

        if result_sum < last_result_sum:
            break
        k = k+1
        total_sum = total_sum + result_sum
    print('Total sum so far', total_sum)
    print('     ')
    return total_sum  # we return only the total sum


one_pi = first_computation() * series_computation()

print('Approximation of 1/pi equals to:', one_pi)
