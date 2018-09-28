steps = list(map(int,input().strip().split()))
steps.sort()
print(steps[2]*steps[0])
