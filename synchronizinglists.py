count=0
while 1:
    tmp = int(input().strip())
    if tmp==0:
        break
    if count!=0:
        print()
    list1=[]
    list2=[]
    for i in range(tmp):
        list1.append(int(input().strip()))
    tmplist1=sorted(list1)
    list1index = [tmplist1.index(i) for i in list1]
    for i in range(tmp):
        list2.append(int(input().strip()))
    tmplist2 = sorted(list2)
    print("\n".join(list(map(str,[tmplist2[i] for i in list1index]))))
    count+=1
