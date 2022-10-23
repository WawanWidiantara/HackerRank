# simple array sum
def simpleArraySum(ar):
    hasil = 0
    for i in ar:
        hasil += i
    return hasil # can use sum(ar)


ar = [1, 2, 3]
print(simpleArraySum(ar))
