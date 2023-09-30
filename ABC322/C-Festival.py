# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc320/tasks/abc322_c

import io
import sys

##########
_INPUT = """\
8 5
1 3 4 7 8
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc322c(n,m,alist):
    alist.append(n)

    for j in range(1,int(alist[0])):
            if (int(alist[0])-j >= 0):
#                print(int(alist[i]),j,int(alist[i])-j)
                print(int(alist[0])-j)
            elif(int(alist[0])-j < 0):
#                print(int(alist[i]),j,int(alist[i+1])-j)
                print(int(alist[1])-j)         


    for i in range(0,m-1):
        for j in range(int(alist[i]),int(alist[i+1])):
                if (int(alist[i])-j >= 0):
#                    print(int(alist[i]),j,int(alist[i])-j)
                    print(int(alist[i])-j)
                elif(int(alist[i])-j < 0):
#                    print(int(alist[i]),j,int(alist[i+1])-j)
                    print(int(alist[i+1])-j)

    print(0)

    for i in range(1,n+1):
        if i <= m:
           ans = m-i
#           print(ans)
        if m < i:
           ans = n-i
#           print(ans)

    return -1


if __name__ == '__main__':
    list = input().split(" ")
    n = int(list[0])
    m = int(list[1])
    alist = input().split(" ")

    abc322c(n,m,alist)
