totalSum=0
for i in range(int(input().strip())):
    num = input().strip()
    power = num[-1]
    num = num[:len(num)-1]
    totalSum += int(num)**int(power)
print(totalSum)
