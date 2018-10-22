with open("input.txt",'r') as f:
    a,b = list(map(int,f.readline().strip().split()))
with open("output.txt",'w') as f:
    f.write(str(a+b))
    f.write('\n')
