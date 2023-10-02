# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abs/tasks/abc088_b

import io
import sys

##########
_INPUT = """\
4
20 18 2 18
"""
sys.stdin = io.StringIO(_INPUT)
##########

def ABC088B(num,list):
    alice = 0
    bob = 0

    list_int = []
    for data in list:
        list_int.append(int(data))

    list_rv = sorted(list_int, reverse=True)

    for i in range(0,num,2):
        alice = alice + list_rv[i]

    for i in range(1,num,2):
        bob = bob + list_rv[i]

    return alice-bob

if __name__ == '__main__':
    num = int(input())
    list  = input().split(" ")
    
    print(ABC088B(num,list))
