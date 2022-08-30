#Q2. Write a python program to print the non-zero elements of a sparse matrix taken as user input in the form of list

sparseMatrix = [[2,4,0,4,5], [0,9,1,4,0], [0,0,2,0,4], [1,6,5,0,3]]

size = 0
for i in range(4):
    for j in range(5):
        if (sparseMatrix[i][j] !=0):
            size += 1


rows, cols = (3, size)
compactMatrix = [[0 for i in range(cols)] for j in range(rows)]
 
k = 0
for i in range(4):
    for j in range(5):
        if (sparseMatrix[i][j] != 0):
            compactMatrix[0][k] = i
            compactMatrix[1][k] = j
            compactMatrix[2][k] = sparseMatrix[i][j]
            k += 1
 
for i in compactMatrix:
    print(i)

