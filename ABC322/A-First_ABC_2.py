# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc322/tasks/abc322_a

import io
import sys

##########
_INPUT = """\
0
""
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc322a(text):

    answer = text.find("ABC")

    if answer == -1:
        return answer
    else:
        return answer+1


if __name__ == '__main__':
    n = input()
    text = input()

    print(abc322a(text))
