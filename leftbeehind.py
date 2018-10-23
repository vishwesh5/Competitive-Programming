while 1:
    x,y = list(map(int,input().strip().split()))
    if x==0 and y==0:
        break
    if x+y==13:
        print("Never speak again.")
    elif x==y:
        print("Undecided.")
    elif x>y:
        print("To the convention.")
    else:
        print("Left beehind.")
