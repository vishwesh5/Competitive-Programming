def main(e,c,left,count):
    count = 0
    while 1:
        #print(e,c,left,count)
        e,c,left,count=getNumOfBottles(e,c,left,count)
        if (e+left)//c == 0:
            break
    print(count)

def getNumOfBottles(e,c,left,count):
    left1 = (e+left)%c
    e1 = (e+left)//c
    left = left1
    count += e1
    e = e1
    return (e,c,left,count)

f,e,c = list(map(int,input().strip().split()))
main(e+f,c,0,0)
