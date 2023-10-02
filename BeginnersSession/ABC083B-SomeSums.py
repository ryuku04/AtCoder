# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abs/tasks/abc083_b

import math

##########
import io
import sys

_INPUT = """\
10 1 2
"""
sys.stdin = io.StringIO(_INPUT)
##########

def getDigitSum(num):
    answer = 0
    a100000 = int(math.floor(num/100000))
    num = num -a100000 * 100000
    a10000 = int(math.floor(num/10000))
    num = num -a10000 * 10000
    a1000 = int(math.floor(num/1000))
    num = num -a1000 * 1000
    a100 = int(math.floor(num/100))
    num = num -a100 * 100
    a10 = int(math.floor(num/10))
    num = num -a10 * 10
    a1 = int(math.floor(num))

    answer = a1 + a10 + a100 + a1000 + a10000 + a100000

    return answer

def ABC083B(num,top,bottom):
    answer = 0

    for i in range(1,num+1):
        digitnum = getDigitSum(i)
        if top <= digitnum and digitnum <= bottom:
            answer = answer + i

    return answer

if __name__ == '__main__':
    textline = input()
    num  = int(textline.split(" ")[0])
    top  = int(textline.split(" ")[1])
    bottom = int(textline.split(" ")[2])

    print(ABC083B(num,top,bottom))
