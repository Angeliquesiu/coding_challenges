# DIAGONAL SUM

# return the sum of the matrix diagonals
# if a number is in both diagonals, only use it once
def diagonalSum(mat):
    summ = 0
    l = len(mat)
    for i in range(l):
        # primary + secondary diagonal
        summ += mat[i][i] + mat[i][-i-1]
    x = l // 2
    # l & 1 means bitwise l & 1
    return summ - mat[x][x] if l & 1 == 1 else summ

# with numpy
def diagonalSum(mat):
    import numpy as np
    summ = sum(np.diag(mat) + np.diag(mat[::-1]))
    x = l // 2
    # l & 1 means bitwise l & 1
    return summ - mat[x][x] if l & 1 == 1 else summ