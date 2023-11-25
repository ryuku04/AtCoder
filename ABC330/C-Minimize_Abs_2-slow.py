# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc330/tasks/abc330_c

import io
import sys

##########
_INPUT = """\
998244353
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc330c(d):
    answer = 0
    answerlist = []

#    print("l=",l,"r=",r) 
#    print("alist=",alist) 

    minlength = 2*10**12
    i = 0
    j = 0
    while(i**2 - d<0):
        j = 0
        if abs(i**2+j**2-d) - minlength < 0:
            minlength = abs(i**2+j**2-d)
#            print("i=",i,"j=",j,"minlength=",minlength)
        i += 1
        while(i**2+j**2-d < 0):
            if abs(i**2+j**2-d) - minlength < 0:
                minlength = abs(i**2+j**2-d)
#                print("i=",i,"j=",j,"minlength=",minlength)
            j += 1

    answer = minlength

    return answer


if __name__ == '__main__':
    d = int(input())

    print(abc330c(d))
