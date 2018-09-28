while 1:
    n = int(input().strip())
    if n==0:
        break
    i=11
    while 1:
        if sum([int(j) for j in str(n*i)])==sum([int(j) for j in str(n)]):
            print(i)
            break
        i+=1
