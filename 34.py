# if the greatest digit is k and there are d digits, then k! <= n <= d*k!
# and also 10^(d-1) <= n < 10^d, so k! < 10^d and 10^(d-1)/d <= k!

import math

factorials = [math.factorial(x) for x in range(0,10)]

def fact_sum(n):
    return sum([factorials[int(x)] for x in str(n)])

for n in range(10, 9 * factorials[9]):
    if n == fact_sum(n):
        print(n)
