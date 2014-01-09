f = open('numbers.txt','r')
matrix = []
for line in f:
    matrix.append([int(x) for x in line.split()])
f.close()

max_product = 0

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i <= len(matrix) - 4:
            max_product = max(max_product, matrix[i][j] * matrix[i+1][j] * matrix[i+2][j] * matrix[i+3][j])
        if j <= len(matrix[0]) - 4:
            max_product = max(max_product, matrix[i][j] * matrix[i][j+1] * matrix[i][j+2] * matrix[i][j+3])
        if i <= len(matrix) - 4 and j <= len(matrix[0]) - 4:
            max_product = max(max_product, matrix[i][j] * matrix[i+1][j+1] * matrix[i+2][j+2] * matrix[i+3][j+3])
            max_product = max(max_product, matrix[i][j+3] * matrix[i+1][j+2] * matrix[i+2][j+1] * matrix[i+3][j])

print(max_product)
