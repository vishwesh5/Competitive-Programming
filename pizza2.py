R,C = list(map(int,input().strip().split()))
print("{:0.9f}".format(100*((R-C)/R)**2))
