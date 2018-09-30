for case in range(int(input().strip())):
    n = int(input().strip())
    guests = list(map(int,input().strip().split()))
    guests_set = set(guests)
    for i in guests_set:
        if guests.count(i) != 2:
            print("Case #{}: {}".format(case+1,i))
            break
