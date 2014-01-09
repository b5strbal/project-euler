from mymath import is_prime
import itertools

def rotate(n):
    s = str(n)
    return int(s[1:] + s[0])

def is_circular_prime(n):
    for i in range(len(str(n))):
        if not is_prime(n):
            return False
        n = rotate(n)
    return True


count = 2
for i in range(1,7):
    for s in itertools.product('1379', repeat = i):
        if is_circular_prime(int("".join(s))):
            count += 1

print(count)
