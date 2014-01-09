f = open('22.txt', 'r')
names = [x.strip('"') for x in f.read().split(',')]
names.sort()

def value(name):
    return sum([ord(x) - 64 for x in name])

print(sum([(i + 1) * value(names[i]) for i in range(len(names))]))
