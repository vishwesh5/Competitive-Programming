while 1:
    try:
        x = input()
    except:
        break
    x = x.strip().split()
    i,j=list(map(int,x))
    print(abs(j-i))
