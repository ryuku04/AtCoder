# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc322/tasks/abc322_c

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
    anslist = []

    for j in range(1,int(alist[0])+1):
#        print(str(int(alist[0])-j))
        anslist.append(str(int(alist[0])-j))

    for i in range(0,m-1):
        for j in range(int(alist[i])+1,int(alist[i+1])+1):
#            print(str(int(alist[i+1])-j))
            anslist.append(str(int(alist[i+1])-j))

    answer = str("\n".join(anslist))

    return answer


if __name__ == '__main__':
    list = input().split(" ")
    n = int(list[0])
    m = int(list[1])
    alist = input().split(" ")

    print(abc322c(n,m,alist))
