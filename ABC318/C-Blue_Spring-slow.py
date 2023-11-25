# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc318/tasks/abc318_c

import io
import sys
import math

##########
_INPUT = """\
8 3 1000000000
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc318c(d,p,flist):
    answer = 0

#    print(d,p,flist)

    flist.sort(reverse=True)

    normalcost = sum(flist)
    allfreepasscost = math.ceil(len(flist)/d)*p

#    print("normalcost",normalcost)
#    print("allfreepasscost",allfreepasscost)

    answer = normalcost

    for ni in range(1,math.ceil(len(flist)/d)):
        for di in range(1,d+1):
            cost = ni*p + sum(flist[(ni-1)*d+di:])
#            print("ni=",ni,"di=",di,"sum_cost=",cost,"freepass=",ni*p,"fslit=",flist[(ni-1)*d+di:])
            if cost < answer:
                answer = cost

    if allfreepasscost < answer:
        answer = allfreepasscost

    return answer


if __name__ == '__main__':
    n,d,p = map(int,input().split())
    flist = list(map(int, sys.stdin.readline().rstrip().split(" ")))

    print(abc318c(d,p,flist))
