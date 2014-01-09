current = 1
total = 1
for i in range(1, 501):
    for j in range(0,4):
        current += 2 * i
        total += current
print(total)
