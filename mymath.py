import math

def fib_list(n):
    """Returns the list of Fibonacci numbers not greater than n."""
    l = []
    a, b = 0, 1
    while b <= n:
        l.append(b)
        a, b = b, a + b
    return l

#phi = (math.sqrt(5) + 1) /2

#def fib(n):
#    return math.floor(phi**n / math.sqrt(5) + 1/2)

def append_next_prime(prime_list):
    """Appends the next prime to a complete list of primes, starting with 2,3."""
    if prime_list == []:
        prime_list = [2]
        return
    elif prime_list == [2]:
        prime_list.append(3)
        return
    else:
        cand = prime_list[-1] + 2
    while True:
        for d in prime_list:
            if d * d > cand:
                prime_list.append(cand)
                return
            elif cand % d == 0:
                cand += 2
                break
        else:
            prime_list.append(cand)
            return

def primes_until(n):
    """Returns the list of positive prime numbers not greater than n."""
    l = [2]
    while l[-1] <= n:
        append_next_prime(l)
    return l[0:-1]

def primes(n):
    """Returns the first n positive primes."""
    l = [2]
    while len(l) < n:
        append_next_prime(l)
    return l

def factor(n):
    assert(n > 0)
    l = []
    d = 2
    new = n
    while True:
        while new % d == 0:
            l.append(d)
            new //= d
        if new == 1:
            return l
        elif new < d * d:
            l.append(new)
            return l
        else:
            d += 1

def is_prime(n):
    """Decides is a number is prime. Efficient only for small numbers."""
    if abs(n) == 2:
        return True
    if abs(n) < 2 or n % 2 == 0:
        return False
    for d in range(3, int(math.sqrt(abs(n))) + 1, 2):
        if n % d == 0:
            return False
    return True

def num_divisors(n):
    assert(n > 0)
    factors = factor(n)
    total = 1
    index = 0
    while(len(factors) > index):
        count = factors.count(factors[index])
        total *= count + 1
        index += count
    return total

def sum_of_proper_divisors(n):
    assert(n > 0)
    factors = factor(n)
    prod = 1
    index = 0
    while(len(factors) > index):
        count = factors.count(factors[index])
        prod *= factors[index] ** (count + 1) - 1
        prod //= factors[index] - 1
        index += count
    return prod - n

def num_digits(n):
    assert(n > 0)
    d = 1
    while 10 ** d < n:
        d += 1
    return d

def get_digit(n, pos):
    """Returns the digit of n at position pos, where pos = 0 is the last digit."""
    return (n // (10**pos)) % 10

#def is_palindrom(n):
#    for i in range(0, num_digits(n) // 2):
#        if get_digit(n, i) != get_digit(n, num_digits(n) - i - 1):
#            return False
#    return True

def is_palindrom(s):
    return s == s[::-1]

numbers_to_words = {
    0 : '',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred'
}

def letter_count(n):
    total = 0
    if n >= 100:
        total += len(numbers_to_words[get_digit(n, 2)]) + len('hundred')
        if n % 100 > 0:
            total += len('and')
    tens = (n % 100) // 10 * 10
    if tens == 10:
        return total + len(numbers_to_words[n % 100])
    elif tens > 10:
        total += len(numbers_to_words[tens])
    return total + len(numbers_to_words[n % 10])
