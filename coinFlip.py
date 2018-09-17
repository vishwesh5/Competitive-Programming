for i in range(int(input().strip())):
    for j in range(int(input().strip())):
        I,N,Q = list(map(int,input().strip().split()))
        if N%2 == 0:
            print(N//2)
        else:
            if Q==I:
                print(N//2)
            else:
                print(N//2 + 1)
