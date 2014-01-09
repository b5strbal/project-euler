f = open('13.txt','r')
numbers = []
for line in f:
    numbers.append(int(line))
f.close()

print(sum(numbers))
