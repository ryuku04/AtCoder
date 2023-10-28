# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc325/tasks/abc325_a

import io
import sys

##########
_INPUT = """\
Takahashi Chokudai
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc325a(s):
    answer = s + " san"
    return answer


if __name__ == '__main__':
    s = input().split(" ")[0]
    print(abc325a(s))
