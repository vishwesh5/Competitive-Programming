seq=[i for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.']
def getRotatedAlphabet(i,rotval):
    initIndex = seq.index(i)
    newIndex = initIndex + rotval
    newIndex = newIndex%len(seq)
    return seq[newIndex]

while 1:
    tmp = input().strip()
    if tmp=="0":
        break
    rotval,string = tmp.split()
    rotval = int(rotval)
    print("".join([getRotatedAlphabet(i,rotval) for i in string[::-1]]))
