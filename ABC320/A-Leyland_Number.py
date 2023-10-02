# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc320/tasks/abc320_a

import io
import sys

##########
_INPUT = """\
5 6
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc320a(a,b):
    answer = a**b + b**a
    
    return answer 

if __name__ == '__main__':
    list = input().split(" ")

    print(abc320a(int(list[0]),int(list[1])))
