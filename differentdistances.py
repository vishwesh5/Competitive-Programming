def printPNormDistance(x1,y1,x2,y2,p):
    dist = (abs(x1-x2)**p + abs(y1-y2)**p)**(1/p)
    print("{:0.10f}".format(dist))

while 1:
    tmp = input().strip()
    if tmp=='0':
        break
    x1,y1,x2,y2,p=list(map(float,tmp.split()))
    printPNormDistance(x1,y1,x2,y2,p)
