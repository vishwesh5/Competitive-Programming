for i in range(int(input().strip())):
    j = int(input().strip())
    stops = list(map(int,input().strip().split()))
    print(2*(max(stops)-min(stops)))
