n,w,h = list(map(int,input().strip().split()))
for i in range(n):
    if (w**2+h**2)**0.5 < int(input().strip()):
        print("NE")
    else:
        print("DA")
