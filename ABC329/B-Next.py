# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc329/tasks/abc329_b

import io
import sys

##########
_INPUT = """\
8
22 22 18 16 22 18 18 22
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc329b(alist):
    answer = 0
    aset = set()

    for a in alist:
        aset.add(int(a))
    
    
    alist_sorted = sorted(list(aset), reverse=True)
#    print(alist_sorted)

    answer = alist_sorted[1]

    return answer


if __name__ == '__main__':
    n = sys.stdin.readline().rstrip()
    alist = sys.stdin.readline().rstrip().split(" ")

    print(abc329b(alist))
