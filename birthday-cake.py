from audioop import reverse


def candle(arr):
    arr.sort(reverse=True)
    n = 0
    for i in arr:
        if i == arr[0]:
            n += 1
    return n

arr = [1,7,2,1,2,3]
print(candle(arr))