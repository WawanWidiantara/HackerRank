def miniMax(arr):
    arr.sort()
    mini = 0
    maxi = 0
    n = len(arr)
    
    for i in arr:
        mini += i
        maxi += i
    
    hasil = [(mini-arr[n-1]), (maxi-arr[0])]
    return hasil

arr = [7, 69, 2, 221, 8974]

print(miniMax(arr))