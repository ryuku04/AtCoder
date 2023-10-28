# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc326/tasks/abc326_a

import io
import sys

##########
_INPUT = """\
1 100
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc326a(x,y):
    answer = "Yes"

    df = x-y
    if 3 < df or df < -2:
        answer = "No"

    return answer


if __name__ == '__main__':
    textline = sys.stdin.readline().rstrip().split(" ")
    x = int(textline[0])
    y = int(textline[1])
    print(abc326a(x,y))
