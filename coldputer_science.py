t = int(input().strip())
temps = list(map(int,input().strip().split()))[:t]
print(len([i for i in temps if i < 0]))
