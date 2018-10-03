for i in range(int(input().strip())):
    str1 = input().strip()
    str2 = input().strip()
    print(str1)
    print(str2)
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            print("*",end="")
        else:
            print(".",end="")
    print("\n")
