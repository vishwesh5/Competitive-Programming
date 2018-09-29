while 1:
    task = input().strip()
    if task=='-1':
        break
    task = int(task)
    totalDist=0
    prevTime =0
    for i in range(task):
        speed,time = list(map(int,input().strip().split()))
        totalDist += speed*(time-prevTime)
        prevTime = time
    print("{} miles".format(totalDist))
