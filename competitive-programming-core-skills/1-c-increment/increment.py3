string = input()
#string = '1'+'0'*1000000
#print(len(string))
flag=False
for i in range(0,9):
    if str(i) in string:
        flag=True
        break
if flag:
    print(len(string))
else:
    print(len(string)+1)
#print(len(str(int(string)+1)))
#print(len(str(int(input().strip())+1)))
