# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc330/tasks/abc330_a

import io
import sys

##########
_INPUT = """\
10 50
31 41 59 26 53 58 97 93 23 84
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc330a(l,alist):
    answer = 0

    for ai in alist :
        score = int(ai)
        if score - l >= 0 :
            answer += 1

    return answer


if __name__ == '__main__':
    alist = []

    n,l = map(int,input().split())
    alist = sys.stdin.readline().rstrip().split(" ")

    print(abc330a(l,alist))
