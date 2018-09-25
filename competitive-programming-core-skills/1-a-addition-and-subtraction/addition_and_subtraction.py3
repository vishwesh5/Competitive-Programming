# -*- coding: utf-8 -*-

import sys

def main():
    x, y, z = map(int, input().split())
    result = -1
    resultOpt = []
    flag=False
    # your code
    if z==0:
        result=0
    elif x==y:
        if z==y:
            result=1
    else:
        try:
            if (z-y)%(x-y)==0:
                tmpResult = 2*(z-y)//(x-y) - 1
                if tmpResult >= 0:
                    resultOpt.append(tmpResult)
                    flag=True
        except:
            pass
        try:
            if z%(x-y)==0:
                tmpResult = 2*z//(x-y)
                if tmpResult >= 0:
                    resultOpt.append(tmpResult)
                    flag=True
        except:
            pass
        if flag:
            result = min(resultOpt)
        if z==0:
            result = 0
    print(result)


if __name__ == '__main__':
    main()
