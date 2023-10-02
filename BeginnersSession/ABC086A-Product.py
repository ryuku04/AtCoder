# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abs/tasks/abc086_a

####################
import io
import sys

_INPUT = """\
72
128 256
myonmyon
"""
sys.stdin = io.StringIO(_INPUT)
####################

def abc086a(a,bc,s):
    b=int(bc.split(" ")[0])
    c=int(bc.split(" ")[1])
    abc = a + b + c
    answer = str(abc) + " " + str(s)
    return answer

if __name__ == '__main__':
    a  = int(input())
    bc = str(input())
    s  = str(input())

    print(abc086a(a,bc,s))
