# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc332/tasks/abc332_b

import io
import sys

##########
_INPUT = """\
10 999 1000
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc332b(k,g,m):
    answer = ""
    gt = 0
    mt = 0

#    print("k=",k,"g=",g,"m=",m)

    for i in range(k):
        if gt == g:
            gt = 0
        elif mt == 0:
            mt = m
        else :
            if mt >= g-gt:
                water = g-gt
                mt -= water
                gt += water
            else:
                water = mt
                mt -= water
                gt += water

#        print("i=",i,"gt=",gt,"mt=",mt)

    answer = str(gt) + " " + str(mt)

    return answer


if __name__ == '__main__':
    k,g,m = map(int,input().split())

    print(abc332b(k,g,m))
