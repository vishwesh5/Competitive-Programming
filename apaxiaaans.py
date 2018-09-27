name = input().strip()
outputName = ''
for i in name:
    if outputName=='':
        outputName+=i
    elif i == outputName[-1]:
        continue
    else:
        outputName+=i
print(outputName)
