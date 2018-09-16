for person in range(int(input().strip())):
    n=int(input())
    headbob=input()[:n]
    if 'I' in headbob:
        print("INDIAN")
    elif 'Y' in headbob:
        print("NOT INDIAN")
    else:
        print("NOT SURE")
