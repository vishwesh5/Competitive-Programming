# -*- coding: utf-8 -*-

import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # your code
    occur = [i for i,n in enumerate(a) if n==max(a)]
    if len(occur)==1:
        del a[occur[0]]
    else:
        del a[occur[2]]

    print(" ".join(map(str,a)))


if __name__ == '__main__':
    main()
