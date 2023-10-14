# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc324/tasks/abc324_b

import io
import sys

##########
_INPUT = """\
37748736
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc324b(n):
    answer = "No"
#    print(n)

    count2 = 0
    n2 = n
    n2temp = -1
    while(n2 != n2temp):
        n2temp = n2
        if(n2 % 2 !=0):
            break
        n2 //= 2
        count2 += 1
#        print(n2,n2temp,count2)
#    print(n2,count2)

    count3 = 0
    n3 = n2
    n3temp = -1
    while(n3 != n3temp):
        n3temp = n3
        if(n3 % 3 !=0):
            break
        n3 //= 3
        count3 += 1
#        print(n3,n3temp,count3)
#    print(n3,count3)

#    print(2 ** count2)
#    print(3 ** count3)
    checkn = 2 ** count2 * 3 ** count3

#    print(checkn)
    if n == checkn:
        answer = "Yes"

    return answer


if __name__ == '__main__':
    n = int(input())
        
    print(abc324b(n))
