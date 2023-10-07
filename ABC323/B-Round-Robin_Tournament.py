# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc323/tasks/abc323_b

import io
import sys

##########
_INPUT = """\
7
-oxoxox
x-xxxox
oo-xoox
xoo-ooo
ooxx-ox
xxxxx-x
oooxoo-
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc323b(list):
    answer = ""
    wonlist = []

    for i in range(len(list)):
#        print(list[i])
        wonlist.append(list[i].count("o"))

#    print(wonlist)

    for i in range(len(wonlist)-1,-1,-1):
        for j in range(0,len(wonlist)):
            if i == int(wonlist[j]):
                answer = answer + str(j+1) + " " 

    answer.rstrip()

    return answer


if __name__ == '__main__':
    list = []
    n = int(input())
    for i in range(0,n):
        list.append(str(input()))
        
    print(abc323b(list))
