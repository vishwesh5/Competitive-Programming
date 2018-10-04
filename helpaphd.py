for i in range(int(input().strip())):
    tmp = input().strip()
    if tmp=="P=NP":
        print("skipped")
    else:
        a,b = list(map(int,tmp.split("+")))
        print(a+b)
