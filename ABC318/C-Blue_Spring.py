# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc318/tasks/abc318_c

import io
import sys
import math

##########
_INPUT = """\
5 2 10
7 1 6 3 6
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc318c(d,p,flist):
    answer = 0

#    print(d,p,flist)

    flist.sort(reverse=True)
#    print(flist)

    normalcost = sum(flist)
    allfreepasscost = math.ceil(len(flist)/d)*p

#    print("normalcost",normalcost)
#    print("allfreepasscost",allfreepasscost)

    answer = normalcost

    i = 0
    cost_sum = 0
    while(i<=len(flist)-1):
        cost_temp = 0
        if i+d > len(flist)-1:
            for j in range(i,len(flist)):
                cost_temp += flist[j]
            if cost_temp >= p:
                cost_sum += p
            else:
                cost_sum += cost_temp
#            print("i=",i,"cost_temp=",cost_temp,"cost_sum=",cost_sum)
            break

        for j in range(i,i+d):
            cost_temp += flist[j]
        if cost_temp >= p:
            cost_sum += p
        else:
            cost_sum += cost_temp
            cost_sum += sum(flist[i+d:len(flist)])
#            print("i=",i,"cost_temp=",cost_temp,"cost_sum=",cost_sum)
            break
        i += d

    if cost_sum < answer:
        answer = cost_sum

    if allfreepasscost < answer:
        answer = allfreepasscost

    return answer


if __name__ == '__main__':
    n,d,p = map(int,input().split())
    flist = list(map(int, sys.stdin.readline().rstrip().split(" ")))

    print(abc318c(d,p,flist))
