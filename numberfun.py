for case in range(int(input().strip())):
    a,b,c = list(map(int,input().strip().split()))
    if a+b == c:
        print("Possible")
    elif abs(a-b) == c:
        print("Possible")
    elif a*b == c:
        print("Possible")
    elif (a/b == c) or (b/a == c):
        print("Possible")
    else:
        print("Impossible")
