# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc324/tasks/abc324_a

import io
import sys

##########
_INPUT = """\
Takahashi Chokudai
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc324a(s):
    answer = s + " san"
    return answer


if __name__ == '__main__':
    s = input().split(" ")[0]
    print(abc324a(s))
