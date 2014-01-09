triangle_numbers = [x * (x + 1) // 2 for x in range(1,50)]

def value(s):
    return sum([ord(s[i]) - 64 for i in range(len(s))])

def is_tr(s):
    if value(s) in triangle_numbers:
        return 1
    else:
        return 0

f = open('42.txt','r')
print(sum([is_tr(s.strip('"')) for s in f.read().split(',')]))
f.close()
