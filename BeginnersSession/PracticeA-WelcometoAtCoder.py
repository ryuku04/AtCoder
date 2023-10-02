# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abs/tasks/practice_1

####################
import io
import sys

_INPUT = """\
1 21
"""
sys.stdin = io.StringIO(_INPUT)
####################

def ABC086A(inputtest):
    answer = "Odd"
    a = int(inputtest.split(" ")[0])
    b = int(inputtest.split(" ")[1])
    if a*b%2 == 0:
        answer = "Even"
    return answer

if __name__ == '__main__':
    inputtest = str(input())

    print(ABC086A(inputtest))
