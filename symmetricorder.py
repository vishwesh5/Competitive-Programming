case=0
while 1:
    n = int(input().strip())
    if n==0:
        break
    tmp = []
    for i in range(n):
        tmp.append(input().strip())
    if n%2==0:
        maxlim=n
    else:
        maxlim=n+1
    print("SET {}".format(case+1))
    for i in range(maxlim//2):
        print(tmp[2*i])
    if maxlim==n:
        maxlim+=2
    for i in range(maxlim//2-1,0,-1):
        print(tmp[2*i-1])
    case+=1
