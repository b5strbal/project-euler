import itertools

def is_pandigital(n):
    return set(str(n)) == {str(x) for x in range(1, len(str(n)) + 1)}

for x in itertools.permutations('7654321'):
    a = int(''.join(x)) 
    if a in Primes():
        print(a)
        break

