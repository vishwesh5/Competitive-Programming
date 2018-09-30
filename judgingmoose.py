l,r = list(map(int,input().strip().split()))
if (l==0) and (r==0):
    print("Not a moose")
else:
    if l!=r:
        print("Odd {}".format(max(l,r)*2))
    else:
        print("Even {}".format(max(l,r)*2))
