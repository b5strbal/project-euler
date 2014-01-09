from math import factorial
remaining = [x for x in range(10)]
so_far = 0

for i in range(10):
    j = 0
    while so_far + (j + 1) * factorial(10 - i - 1) < 1000000:
        j += 1
    so_far += j * factorial(10 - i - 1)
    print(remaining.pop(j))
