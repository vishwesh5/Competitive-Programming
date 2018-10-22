with open("input.txt",'r') as f:
    A0,A1,A2,n = list(map(int,f.readline().strip().split()))

An = [A0,A1,A2]

while len(An) < n+1:
    tn = len(An)
    prev3 = An[tn-3]
    prev2 = An[tn-2]
    prev1 = An[tn-1]
    An.append(prev1+prev2-prev3)

def getAn(n):
    global A0
    global A1
    global A2
    if n == 0:
        return A0
    elif n==1:
        return A1
    elif n==2:
        return A2
    elif n>=3:
        return getAn(n-1)+getAn(n-2)-getAn(n-3)

with open("output.txt",'w') as f:
    f.write(str(An[n]))
    f.write("\n")
