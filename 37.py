from mymath import is_prime

def find_r_truncatables(n):
    """Returns the list or right-truncatable primes beginning with n."""
    if is_prime(n):
        l = [n]
    else:
        return []
    for i in '1379':
        l.extend(find_r_truncatables(int(str(n) + i)))
    return l

def is_l_truncatable(n):
    if not is_prime(n):
        return False
    if n in [2, 3, 5, 7]:
        return True
    return is_l_truncatable(int(str(n)[1:]))


r_truncatables = sum([find_r_truncatables(n) for n in [2,3,5,7]], [])
print(sum([x for x in  r_truncatables if is_l_truncatable(x) and x > 10]))
