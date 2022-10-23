def diagonalDifference(a):
    kanan = 0
    kiri = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if i == j:
                kanan += a[i][j]
                kiri += a[i][len(a) - (1 + j)]
    hasil = kanan - kiri
    return abs(hasil)
 
a = [[1,2,3], 
     [4,5,6], 
     [9,8,9]]

print(diagonalDifference(a))