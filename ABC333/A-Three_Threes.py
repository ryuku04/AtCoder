# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc333/tasks/abc333_a

import io
import sys

##########
_INPUT = """\
9
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc333a(n):
    answer = ""

    for i in range(n):
        answer += str(n)
   
    return answer


if __name__ == '__main__':
    n = int(input())

    print(abc333a(n))
