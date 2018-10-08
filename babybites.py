n = int(input().strip())
inputs = input().strip().split()
flag=False
for i in range(n):
    #print(inputs,inputs[i])
    if i == 0 and inputs[i]=='mumble':
        inputs[i]=1
    else:
        if i==0:
            continue
        elif inputs[i]=='mumble':
            inputs[i]=int(inputs[i-1])+1
        else:
            if int(inputs[i])-int(inputs[i-1])!=1:
                flag=True
                break

#print(inputs)
if flag:
    print("something is fishy")
else:
    print("makes sense")
