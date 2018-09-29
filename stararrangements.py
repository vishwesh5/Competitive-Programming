z = int(input().strip())
print("{}:".format(z))
if z%2==0:
    maxLim = z//2
else:
    maxLim = (z+1)//2
for x in range(2,maxLim+1):
    for i in [-1,0]:
        y = x+i
        if z%(x+y)==0 or (z+y)%(x+y)==0:
            print("{},{}".format(x,y))
