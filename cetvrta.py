x_index=[]
y_index=[]
for i in range(3):
    index = list(map(int,input().strip().split()))
    x_index.append(index[0])
    y_index.append(index[1])
x_unique,y_unique = set(x_index),set(y_index)
for x in x_unique:
    if x_index.count(x)!=2:
        x_point=x
        break
for y in y_unique:
    if y_index.count(y)!=2:
        y_point=y
        break
print("{} {}".format(x_point,y_point))
