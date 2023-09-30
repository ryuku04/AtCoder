# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc321/tasks/abc321_a

import io
import sys

##########
_INPUT = """\
86411
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc321a(n):
    nlist = list(n)
    answer = "Yes"

    for i in range(1,len(nlist)):
        if nlist[i-1]<=nlist[i]:
            answer = "No"

    return answer


if __name__ == '__main__':
    n = str(input())

    print(abc321a(n))
