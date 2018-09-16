# problem link: https://www.codechef.com/problems/ONP

for task in range(int(input().strip())):
    expression = input()
    listExp = []
    symbols = []
    count   = 0
    for i in expression:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
            symbol = symbols.pop()
            listExp.append(symbol)
        elif i.isalpha():
            listExp.append(i)
        else:
            symbols.append(i)
    print(''.join(listExp))
