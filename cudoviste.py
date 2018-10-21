parkingplot = []
R,C = list(map(int,input().strip().split()))
#parkingrow = []
for i in range(R):
    parkingrow = [i for i in input().strip()]
    parkingplot.append(parkingrow)
#print(parkingplot)
parkings = {0:0, 1:0, 2:0, 3:0, 4:0}
for i in range(R-1):
    #submat=[]
    j=0
    while j+2 <= C:
        submat=[]
        for row in range(2):
            for col in range(2):
                submat.append(parkingplot[i+row][j+col])
        j+=1
        #print(parkings,submat)
        if '#' in submat:
            continue
        else:
            parkings[submat.count('X')]+=1
        #print(parkings,submat)
for i in range(5):
    print(parkings[i])
