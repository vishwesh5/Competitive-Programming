cups={}
for i in range(int(input().strip())):
    task = input().split()
    if task[0].isnumeric() == True:
        cups[int(task[0])//2] = task[1]
    else:
        cups[int(task[1])] = task[0]
cupR = list(cups.keys())
cupR.sort()
for i in cupR:
    print(cups[i])
