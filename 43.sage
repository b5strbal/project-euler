from itertools import permutations

primes = [2,3,5,7,11,13,17]
good_numbers = []

def find_good_numbers(num_sofar, remaining):
    if len(remaining) == 0:
        good_numbers.append(int(num_sofar))
        return
    for next_digit in remaining:
        new_num = num_sofar + next_digit
        if len(num_sofar) == 0 and next_digit == '0' or\
                len(new_num) >= 4 and int(new_num[-3:]) % primes[len(new_num) - 4] != 0:
                    continue
        new_remaining = list(remaining)
        new_remaining.remove(next_digit)
        find_good_numbers(new_num, new_remaining)

find_good_numbers('', list('0123456789'))
print(sum(good_numbers))
