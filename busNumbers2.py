n = int(input().strip())
busNums = list(map(int,input().strip().split()))[:n]
busNums.sort()
i=0
output=[]
consCount=0
while i<n-1:
    if busNums[i+1]-busNums[i]==1:
        if consCount==0:
            output.append(str(busNums[i]))
        consCount+=1
    else:
        if consCount<=1:
            output.append(str(busNums[i]))
        else:
            output[-1]=output[-1]+"-"+\
                    str(busNums[i])
        consCount=0
    i+=1
if consCount<=1:
    output.append(str(busNums[i]))
else:
    output[-1]=output[-1]+"-"+\
            str(busNums[i])

print(' '.join(output))
