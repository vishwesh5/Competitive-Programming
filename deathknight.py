count=0
for i in range(int(input().strip())):
    tmp = input().strip()
    if 'CD' in tmp:
        continue
    count+=1
print(count)
