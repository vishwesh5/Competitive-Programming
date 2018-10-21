N,T = list(map(int,input().strip().split()))
tasks = list(map(int,input().strip().split()))[:N]
count=0
time = 0
for i in tasks:
    if time + i > T:
        break
    time = time+i
    count+=1
print(count)
