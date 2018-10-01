allowed,num = list(map(int,input().strip().split()))
initCount = 0
notAllowed = 0
for i in range(num):
    action,numPeople = input().strip().split()
    numPeople = int(numPeople)
    if action=="enter":
        if initCount + numPeople > allowed:
            notAllowed += 1
        else:
            initCount += numPeople
    else:
        initCount -= numPeople
print(notAllowed)
