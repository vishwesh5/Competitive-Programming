rems = []
for i in range(10):
    num = int(input().strip())
    rems.append(num%42)
print(len(set(rems)))
