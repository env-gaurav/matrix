matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# Element access
print(matrix)
print(matrix[1][0])
print(matrix[2][0])
print(matrix[0][0])

# Element modification
matrix[1][1]=15

## multiply all the coloumns of indices 1 by 2.
for i in range(len(matrix[1])):
    matrix[1][i]*=2
print(matrix)

## subtract all the coloumns of indices 2 by 2.
for i in range(len(matrix[2])):
    matrix[2][i]-=2
print(matrix)

## multiply entire matrix by 2. 
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j]*=2
print(matrix)