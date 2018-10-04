from math import pi

while 1:
    r,m,c = input().strip().split()
    r = float(r)
    m,c = int(m),int(c)
    if r==0.0 and m==0 and c==0:
        break
    print("{:0.9f} {:0.9f}".format(pi*r**2,c/m*(4*r**2)))
