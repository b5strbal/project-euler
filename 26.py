def length_of_cycle(n):
    """Length of repeating cycle in 1/n."""
    assert(n > 0)
    oddpart = n
    while oddpart % 2 == 0:
        oddpart //= 2
    while oddpart % 5 == 0:
        oddpart //= 5       
    if oddpart == 1:
        return 0
    length = 1
    while (10 ** length - 1) % oddpart != 0:
        length += 1
    return length

current_max = 1
for n in range(1,1000):
    if length_of_cycle(current_max) < length_of_cycle(n):
        current_max = n
print(current_max)

    
