import math
for task in range(int(input().strip())):
    v0,t,x1,h1,h2=list(map(float,input().strip().split()))
    t1 = x1/(v0*math.cos(math.radians(t)))
    y1 = v0*t1*math.sin(math.radians(t))-0.5*9.81*t1**2
    if y1 < h2-1 and y1 > h1+1:
        print("Safe")
    else:
        print("Not Safe")
