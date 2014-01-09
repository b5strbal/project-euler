def is_9pandigital(n):
    return set('123456789') == set(str(n))


results = []

for n in range(1,10000):
    s = ''
    for i in range(1,10):
        s += str(n * i)
        if len(s) == 9 and is_9pandigital(s):
            results.append(int(s))
        elif len(s) >= 9:
            break

print(sorted(results))
