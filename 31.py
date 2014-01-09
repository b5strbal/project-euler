coins = [1, 2, 5, 10, 20, 50, 100, 200]

def num_partitions(n, coins):
    if coins == [1]:
        return 1
    if n == 0:
        return 1
    total = 0
    d = 0
    while n - coins[-1] * d >= 0:
        total += num_partitions(n - coins[-1] * d, coins[:-1])
        d += 1
    return total

print(num_partitions(200, coins))
