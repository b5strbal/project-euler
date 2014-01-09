digits = ''
for i in range(1,100000):
    digits += str(i)
    if len(digits) >= 1000000:
        break

print(prod([int(digits[10**i - 1]) for i in range(6)]))


