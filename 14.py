values = {1 : 1}

def it(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def get_value(values, n):
    if n in values.keys():
        return values[n]
    else:
        v = get_value(values, it(n)) + 1
        values[n] = v
        return v

best_key = 1
for i in range(1,1000000):
    get_value(values, i)
    if values[best_key] < values[i]:
        best_key = i

print(best_key)


