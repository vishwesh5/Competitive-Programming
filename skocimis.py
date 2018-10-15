A,B,C = list(map(int,input().strip().split()))
if B-A >= C-B:
    print(B-A-1)
else:
    print(C-B-1)
