def checkAmbiguousPermutation(permut):
    index = 1
    for i in permut:
        if permut[i-1] != index:
            return False
        index+=1
    return True

while 1:
    n = int(input().strip())
    if n==0:
        break
    permut = list(map(int,input().strip().split()))
    permut = permut[:n]
    if checkAmbiguousPermutation(permut):
        print("ambiguous")
    else:
        print("not ambiguous")
