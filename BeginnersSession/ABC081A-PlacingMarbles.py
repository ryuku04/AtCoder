# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abs/tasks/abc081_a

##########
import io
import sys

_INPUT = """\
000
"""
sys.stdin = io.StringIO(_INPUT)
##########

def ABC081A(inputtest):
    s = list(inputtest)
    answer=0
    for st in s:
        if st =="1":
            answer += 1
    return answer

if __name__ == '__main__':
    inputtest  = str(input())

    print(ABC081A(inputtest))
