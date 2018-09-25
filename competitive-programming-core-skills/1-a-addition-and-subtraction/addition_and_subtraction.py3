# -*- coding: utf-8 -*-

import sys

def main():
    x, y, z = map(int, input().split())
    result = -1

    # your code
    if z == 0:
        result = 0
    elif (z-y)%(x-y)==0:
        result = 2*(z-y)//(x-y) - 1
    elif z%(x-y)==0:
        result = 2*z/(x-y)+1
    print(result)


if __name__ == '__main__':
    main()
