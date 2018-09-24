h,m = list(map(int,input().strip().split()))
if m >= 45:
    outputm = m-45
    outputh = h
else:
    outputm = 60+m - 45
    if h == 0:
        outputh = 23
    else:
        outputh = h-1
print(outputh,outputm)
