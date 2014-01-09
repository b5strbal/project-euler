from itertools import permutations

def is_pan_digital(str_n):
    if len(str_n) != 9:
        return False
    for i in '123456789':
        if i not in str_n:
            return False
    return True

products = set()

def test_product(str_a, str_b):
    c = int(str_a) * int(str_b)
    if is_pan_digital(str(c) + str_a + str_b):
        products.add(c)

for x in permutations('123456789', 5):
    test_product(x[0], ''.join(x[1:]))
    test_product(x[0] + x[1], ''.join(x[2:]))

print(sum(products))
