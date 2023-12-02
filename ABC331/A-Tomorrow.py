# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc331/tasks/abc331_a

import io
import sys

##########
_INPUT = """\
12 30
2023 12 30
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc331a(mm,dd,y,m,d):
    
    nexty = y
    nextm = m
    nextd = d + 1

    if nextd > dd:
        nextd = 1
        nextm = m +1
        if nextm > mm:
            nextm = 1
            nexty = y +1

    answer = str(nexty) + " " + str(nextm) + " " + str(nextd)

    return answer


if __name__ == '__main__':
    alist = []

    mm,dd = map(int,input().split())
    y,m,d = map(int,input().split())

    print(abc331a(mm,dd,y,m,d))
