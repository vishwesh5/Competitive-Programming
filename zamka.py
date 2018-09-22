L = int(input())
D = int(input())
X = int(input())

minIntFlag=False
maxIntFlag=False

num1=L
num2=D

def sumOfNum(num):
    return sum([int(i) for i in str(num)])

while not (minIntFlag and maxIntFlag):
#    print(num1,num2)
    if not minIntFlag and sumOfNum(num1)==X:
        minInt=num1
        minIntFlag=True
    else:
        num1+=1

    if not maxIntFlag and sumOfNum(num2)==X:
        maxInt=num2
        maxIntFlag=True
    else:
        num2-=1
print(minInt)
print(maxInt)
