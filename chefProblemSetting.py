# problem link: https://www.codechef.com/LTIME63B/problems/PROBSET
for i in range(int(input().strip())):
    N,M = list(map(int,input().strip().split(" ")))
    answer = "FINE"
    for j in range(N):
        test,outputs = input().strip().split(" ")
        if test=="correct":
            if '0' in outputs:
                answer = "INVALID"
        else:
            if '0' not in outputs:
                if answer != "INVALID":
                    answer = "WEAK"
            else:
                if (answer != "WEAK") and (answer!="INVALID"):
                    answer="FINE"
    print(answer)
