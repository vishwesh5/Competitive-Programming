for i in range(int(input().strip())):
    K,N = list(map(int,input().strip().split()))
    print("{} {} {} {}".format(K,N*(N+1)//2,N**2,N*(N+1)))
