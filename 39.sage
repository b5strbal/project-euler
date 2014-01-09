# a^2 - b^2, 2ab, a^2 + b^2
# 2a^2 + 2ab = 2a(a + b)

sums_of_primitive_triples = [2 * a * (a + b) for a in range(2,25) for b in range(1,a) if 2 * a * (a + b) <= 1000 and gcd(a,b) == 1 and (a*b) % 2 == 0]

print(sums_of_primitive_triples)

all_sums = [x * n for x in sums_of_primitive_triples for n in range(1,1000//x + 1)] 

print(sorted(all_sums))

print(max(all_sums, key = (lambda x: all_sums.count(x))))
