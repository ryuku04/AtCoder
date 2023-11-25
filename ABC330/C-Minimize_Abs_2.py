# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc330/tasks/abc330_c

import io
import sys
import math

##########
_INPUT = """\
264428617
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc330c(d):
    answer = 0

    minlength = 2*10**12
    i = 0
    j = 0
    while(j**2-d/2<0):
        i = int(math.floor(math.sqrt(d-j**2)))
#        print("i=",i,"j=",j,"abs=",abs(i**2+j**2-d),"minlength=",minlength)
        if abs(i**2 + j**2 - d) - minlength < 0:
            minlength = abs(i**2+j**2-d)
#            print("lengh=",abs(i**2 - j**2 - d) - minlength)
        i = i + 1
        if abs(i**2 + j**2 - d) - minlength < 0:
            minlength = abs(i**2+j**2-d)
#            print("lengh=",abs(i**2 - j**2 - d) - minlength)
        j+=1

    if j**2-d/2<0:
        i = int(math.floor(math.sqrt(d-j**2)))
#        print("i=",i,"j=",j,"abs=",abs(i**2+j**2-d),"minlength=",minlength)
        if abs(i**2 + j**2 - d) - minlength < 0:
            minlength = abs(i**2+j**2-d)
#            print("lengh=",abs(i**2 - j**2 - d) - minlength)
        i = i + 1
        if abs(i**2 + j**2 - d) - minlength < 0:
            minlength = abs(i**2+j**2-d)
#            print("lengh=",abs(i**2 - j**2 - d) - minlength)

    if j**2-d/2>=0:
        i = 0
#        print("i=",i,"j=",j,"abs=",abs(i**2+j**2-d),"minlength=",minlength)
        if abs(i**2 + j**2 - d) - minlength < 0:
            minlength = abs(i**2+j**2-d)
#            print("lengh=",abs(i**2 - j**2 - d) - minlength)
        i = i + 1
        if abs(i**2 + j**2 - d) - minlength < 0:
            minlength = abs(i**2+j**2-d)
#            print("lengh=",abs(i**2 - j**2 - d) - minlength)


    answer = minlength

    return answer


if __name__ == '__main__':
    d = int(input())

    print(abc330c(d))
