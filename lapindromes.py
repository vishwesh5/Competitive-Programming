def getSubstr(string):
    if len(string)%2==0:
        str_1 = string[:len(string)//2]
        str_2 = string[len(string)//2:]
    else:
        str_1 = string[:(len(string)-1)//2]
        str_2 = string[(len(string)+1)//2:]
    return str_1,str_2

def char_frequency(string):
    char_dict={}
    for n in string:
        keys = char_dict.keys()
        if n in keys:
            char_dict[n] += 1
        else:
            char_dict[n] = 1
    return char_dict

def matchDicts(dict1, dict2):
    if dict1.keys() == dict2.keys():
        for n in dict1.keys():
            if dict1[n] != dict2[n]:
                return False
    else:
        return False
    return True

for i in range(int(input().strip())):
    string = input().strip()
    str1,str2 = getSubstr(string)
    d1,d2 = char_frequency(str1),char_frequency(str2)
    if d1 == d2:
        print("YES")
    else:
        print("NO")
