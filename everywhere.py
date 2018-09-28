for task in range(int(input().strip())):
    n = int(input().strip())
    places=[]
    for i in range(n):
        places.append(input().strip())
    print(len(set(places)))
