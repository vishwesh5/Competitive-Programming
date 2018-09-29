for i in range(int(input().strip())):
    counts = list(map(int,input().strip().split()))
    immigrants=0
    for n in range(1,len(counts)-1):
        tmp = counts[n]-2*counts[n-1]
        if tmp > 0:
            immigrants+=tmp
    print(immigrants)
