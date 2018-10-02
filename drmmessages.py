def divide(encodedstr):
    return (encodedstr[:len(encodedstr)//2], encodedstr[len(encodedstr)//2:])

def rotate(encodedstr):
    rotvalue = sum([ord(i)-ord('A') for i in encodedstr])
    tmpOrd = [ord(i)-ord('A') for i in encodedstr]
    tmpOrdMod = [(i+rotvalue)%26 for i in tmpOrd]
    newencodedstr = [chr(i+ord('A')) for i in tmpOrdMod]
    newencodedstr = ''.join(newencodedstr)
    return newencodedstr

def merge(encodedstr1, encodedstr2):
    rotvalues = [ord(i)-ord('A') for i in encodedstr2]
    tmpstr1 = [ord(i)-ord('A') for i in encodedstr1]
    tmpstr1mod = [(tmpstr1[i]+rotvalues[i])%26 for i in range(len(rotvalues))]
    newencodedstr1 = [chr(i+ord('A')) for i in tmpstr1mod]
    newencodedstr1 = ''.join(newencodedstr1)
    return newencodedstr1

def main():
    encodedstr = input().strip()
    str1,str2 = divide(encodedstr)
    str1,str2 = rotate(str1),rotate(str2)
    str1 = merge(str1,str2)
    print(str1)

if __name__=="__main__":
    main()
