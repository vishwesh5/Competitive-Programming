from math import pi

while 1:
    D,V = list(map(int,input().strip().split()))
    if D==0 and V==0:
        break
    d = (D**3 - 6*V/pi)**(1/3)
    print("{:0.9f}".format(d))
