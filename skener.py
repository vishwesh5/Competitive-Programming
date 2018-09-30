r,c,zr,zc = list(map(int,input().strip().split()))
for i in range(r):
    chars = input().strip()
    for col in range(zr):
        for char in chars:
            print(char*zc,end="")
        print("")
