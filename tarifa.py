X=int(input().strip())
N=int(input().strip())
dataLeft=0
for i in range(N):
    dataUsed=int(input().strip())
    dataLeft=X-dataUsed+dataLeft
print(X+dataLeft)
