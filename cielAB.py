A,B = list(map(int,input().strip().split()))
ans = [i for i in str(A-B)]
if (ans[0] != '1'):
    ans[0]='1'
else:
    ans[0]='2'
print(''.join(ans))
