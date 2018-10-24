total_min = 0
total_sec = 0
for i in range(int(input().strip())):
    a,b = list(map(int,input().strip().split()))
    total_min += a
    total_sec += b
#print(total_min,total_sec)
avg_length = total_sec/(total_min*60)
if avg_length <= 1.0:
    print("measurement error")
else:
    print("{:.9f}".format(total_sec/(total_min*60)))
