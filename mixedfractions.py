while 1:
    a,b = list(map(int,input().strip().split()))
    if a==b and a==0:
        break
    print("{} {} / {}".format(a//b,a%b,b))
