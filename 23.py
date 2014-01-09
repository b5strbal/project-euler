from mymath import sum_of_proper_divisors

def is_abundant(n):
    return sum_of_proper_divisors(n) > n

ab_numbers = [x for x in range(1, 28124) if is_abundant(x)]
print(len(ab_numbers))
sums = {x + y for x in ab_numbers for y in ab_numbers}
print(len(sums))

print(sum([x for x in range(1,28124) if x not in sums]))

