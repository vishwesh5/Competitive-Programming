n,p,q = list(map(int,input().strip().split()))
a = (p+q)//n+1
if a % 2 == 0:
    print("opponent")
else:
    print("paul")
