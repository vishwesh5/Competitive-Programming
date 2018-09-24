h,v = list(map(int,input().strip().split()))
import math

def sind(theta):
    return math.sin(math.radians(theta))

print(math.ceil(h/sind(v)))
