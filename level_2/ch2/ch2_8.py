def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j],end=" ")
        print()

'''
list2x3 = [[1,5,6],
               [7,2,9]]

printMatrix(list2x3)
'''
matrixA = []

for i in range(2):
    row = []
    for  j in range(3):
        row.append((i+1) **2 + (j+2)**2)
    matrixA.append(row)
printMatrix(matrixA)    
