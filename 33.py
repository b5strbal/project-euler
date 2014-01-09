from fractions import Fraction

def is_curious(num, denom):
    s = str(num) + str(denom)
    if '0' in s:
        return False
    if str(num)[0] == str(denom)[1]:
        if num * int(str(denom)[0]) == denom * int(str(num)[1]):
           return True
    else:
        return False

curious_fracs = []

for num in range(11,100):
    for denom in range(num + 1, 100):
        if is_curious(num, denom) or is_curious(denom, num):
           curious_fracs.append(Fraction(num, denom))

print(curious_fracs)
