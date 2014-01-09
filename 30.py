# if a n has d digits, then 10**(d-1) <= n <= d * 9**5
# so d <= 6 and n <= 354294

fifth_powers = [x**5 for x in range(10)]
total = 0
for n in range(2, 354294):
    if n == sum([fifth_powers[int(x)] for x in str(n)]):
        total += n
print(total)
