caseNum=0
while 1:
    try:
        x,y,r=list(map(float,input().strip().split()))
    except:
        break
    c = complex(x,y)
    z = complex(0,0)
    r = int(r)
    diverges=False
    for i in range(r):
        z = z*z+c
        if abs(z) > 2:
            diverges=True
            break
#        z = z*z + c
    if diverges==False:
        print("Case {}: IN".format(caseNum+1))
    else:
        print("Case {}: OUT".format(caseNum+1))
    caseNum+=1
