def compareTripplets(a, b):
    alice = 0
    bob = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
    hasil = [alice, bob]
    return hasil


a = [1, 2, 3]
b = [3, 2, 1]

print(compareTripplets(a, b))
