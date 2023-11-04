# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc319/tasks/abc319_b

import io
import sys

##########
_INPUT = """\
12
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc319b(number):
    answer = ""

    for i in range(0,number+1):
        for j in range(1,10):
            if number%j == 0 and i%(number/j) == 0:
#                print("i=",i,"j=",j)
                answer += str(j)
                break
            if j == 9:
                answer += "-"

    return answer 

if __name__ == '__main__':
    number = int(input())

    print(abc319b(number))
