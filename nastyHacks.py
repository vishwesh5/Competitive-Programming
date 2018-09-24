for i in range(int(input().strip())):
    r,e,c=list(map(int,input().strip().split()))
    if e-r==c:
        print("does not matter")
    elif e-r>c:
        print("advertise")
    else:
        print("do not advertise")
