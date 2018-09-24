awards=0
univCovered = []
for i in range(int(input().strip())):
    univ,team=input().strip().split()
    if awards==12:
        continue
    if univ in univCovered:
        continue
    else:
        print("{} {}".format(univ,team))
        awards+=1
        univCovered.append(univ)
