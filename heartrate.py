for i in range(int(input().strip())):
    b,p = input().strip().split()
    b = int(b)
    p = float(p)
    print("{:0.4f} {:0.4f} {:0.4f}".format(60*(b-1)/p, 60*b/p, 60*(b+1)/p))
