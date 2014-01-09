from mymath import is_prime

maxstreak = 0
for a in range(-999, 1000):
    for b in range(-999, 1000):
        n = 0
        while is_prime(n * n + a * n + b):
            n += 1
        if maxstreak < n:
            maxstreak, maxa, maxb = n, a, b

print(maxa * maxb)
