def diagonalDifference(a):
    kanan = 0
    kiri = 0

    # for i in range(len(a)):
    #     for j in range(len(a[0])):
    #         if i == j:
    #             kanan += a[i][j]
    #             kiri += a[i][len(a) - (1 + j)]

    # cara 2
    n = len(a)
    for i in range(n):
        kanan += a[i][i]
        kiri += a[i][n - i - 1]

    return abs(kanan - kiri)


a = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]

print(diagonalDifference(a))
