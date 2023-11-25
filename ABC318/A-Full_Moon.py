# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc318/tasks/abc318_a

import io
import sys

##########
_INPUT = """\
200000 314 318
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc318a(n,m,p):
    answer = 0
    
    if n < m:
        return answer
    
    answer = int((n-m)/p) + 1

    return answer


if __name__ == '__main__':
    n,m,p = map(int,input().split())

    print(abc318a(n,m,p))
