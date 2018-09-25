# -*- coding: utf-8 -*-

import sys

def main():
    x, y, z = map(int, input().split())
    result = -1
    resultOpt = []
    flag=False
    # your code
    if (z-y)%(x-y)==0:
        resultOpt.append(2*(z-y)//(x-y) - 1)
        flag=True
    if z%(x-y)==0:
        resultOpt.append(2*z//(x-y)+1)
        flag=True
    if flag:
        result = min(resultOpt)
    if z==0:
        result = 0
    print(result)


if __name__ == '__main__':
    main()
