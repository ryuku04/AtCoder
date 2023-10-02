# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abs/tasks/abc085_b

import io
import sys

##########
_INPUT = """\
7
50
30
50
100
50
80
30
"""
sys.stdin = io.StringIO(_INPUT)
##########

def ABC085B(num,list):
    list_set = set(list)
    return len(list_set)

if __name__ == '__main__':
    list = []
    num = int(input())
    for i in range(0,num):
        list.append(int(input()))

    print(ABC085B(num,list))
