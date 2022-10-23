def staircase(n):
    for i in range(n):
        tag = '#' * (i+1)
        space = ' ' * (n-i-1)
        print(space+tag)
    
n = 6
staircase(n)