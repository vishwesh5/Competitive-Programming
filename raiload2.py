x,y = list(map(int,input().strip().split()))
if (3*y+4*x)%2==0:
    print("possible")
else:
    print("impossible")
