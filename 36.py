def is_palindrom(s):
    return s == s[::-1]

print(sum([n for n in range(1, 1000000) if is_palindrom(str(n)) and is_palindrom(bin(n)[2:])]))
