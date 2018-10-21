listCount=0
while 1:
    n = int(input().strip())
    if n==0:
        break
    listCount+=1
    animals = {}
    for i in range(n):
        animal = input().strip().split()
        animaltype = animal[-1].lower()
        if animaltype not in animals.keys():
            animals[animaltype]=1
        else:
            animals[animaltype]+=1
    print("List {}:".format(listCount))
    animaltypes = [i for i in animals.keys()]
    animaltypes.sort()
    for i in animaltypes:
        print("{} | {}".format(i,animals[i]))
