# problem link: https://www.codechef.com/problems/PALL01

for i in range(int(input().strip())):
    N = input().strip()
    if N == N[::-1]:
        print("wins")
    else:
        print("losses")
