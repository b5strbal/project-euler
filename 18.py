f = open('67.txt','r')
data = []
totals = []
for line in f:
    data.append([int(x) for x in line.split()])
    totals.append([0 for x in line.split()])
f.close()

totals[0][0] = data[0][0]
for i in range(1,len(data)):
    totals[i][0] = data[i][0] + totals[i-1][0]
    totals[i][-1] = data[i][-1] + totals[i-1][-1]
    for j in range(1,len(data[i])-1):
        totals[i][j] = data[i][j] + max(totals[i-1][j], totals[i-1][j-1])

#for x in data:
#    print(x)
#for x in totals:
#    print(x)

print(max(totals[-1]))
