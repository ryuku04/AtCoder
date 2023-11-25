# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc330/tasks/abc330_b

import io
import sys

##########
_INPUT = """\
3 10 10
11 10 9
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc330b(l,r,alist):
    answer = 0
    answerlist = []

#    print("l=",l,"r=",r) 
#    print("alist=",alist) 

    for a in alist:
        if l - int(a) >= 0:
            answerlist.append(str(l))
        elif int(a) - r >= 0:
            answerlist.append(str(r))
        elif r - int(a) > 0 and int(a) - l > 0:
            answerlist.append(a)
        else :
            answerlist.append("error")

    answer = " ".join(answerlist)

    return answer


if __name__ == '__main__':
    n,l,r = map(int,input().split())
    alist = sys.stdin.readline().rstrip().split(" ")

    print(abc330b(l,r,alist))
