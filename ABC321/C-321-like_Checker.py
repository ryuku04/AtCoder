# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc321/tasks/abc321_c

import io
import sys

##########
_INPUT = """\
321
"""
sys.stdin = io.StringIO(_INPUT)
##########


def abc321c(n):
    anslist=[]

    for i in range(1,10):
        anslist.append(str(i))
#            print(str(i))

    for i in range(10, 9876543211):
        nlist = list(str(i))

        flg = True
        for j in range(1,len(nlist)):
            if nlist[j-1]<=nlist[j]:
                flg = False
                break
        if flg == True:
            anslist.append(str(i))
#            print(str(i))

        if len(anslist) == n:
            answer = anslist[n-1]
            break

    return answer


if __name__ == '__main__':
    n = int(input())

    print(abc321c(n))
