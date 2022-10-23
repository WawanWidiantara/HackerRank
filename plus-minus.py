def plusMinus(arr):
    n = len(arr)
    plus = 0
    minus = 0
    zero = 0

    for i in arr:
        if i < 0:
            minus += 1
        elif i > 0:
            plus += 1
        else:
            zero += 1

    hasil = [(plus / n), (minus / n), (zero / n)]

    for h in hasil:
        print(h)


arr = [0, 0, -1, 1, 1]

plusMinus(arr)
