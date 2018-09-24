costSq=float(input().strip())
totalSum=0
for i in range(int(input().strip())):
    w,h=list(map(float,input().strip().split()))
    totalSum += w*h
print("{:0.7f}".format(totalSum*costSq))
