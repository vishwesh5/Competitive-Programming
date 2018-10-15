def encodeText(text):
    out=''
    i = 0
    count=1
    while i<len(text)+1:
        if i==0:
            i+=1
            continue
        elif i==len(text):
            out=out+text[i-1]
            out=out+str(count)
        else:
            if text[i]==text[i-1]:
                count+=1
            else:
                out=out+text[i-1]
                out=out+str(count)
                count=1
        i+=1
    return out

def decodeText(text):
    out=''
    i=0
    while i<len(text)//2:
        ch = text[2*i]
        count=text[2*i+1]
        out=out+ch*int(count)
        i+=1
    return out

mode,text=input().strip().split(" ")
if mode=="E":
    print(encodeText(text))
elif mode=='D':
    print(decodeText(text))
