# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc329/tasks/abc329_a

import io
import sys

##########
_INPUT = """\
OOXXOO
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc329a(text):
    answer = ""

    for i in range(len(text)):
        answer = answer + text[i] + " "

    answer = answer.rstrip('\r\n')

    return answer


if __name__ == '__main__':
    text = sys.stdin.readline().rstrip()

    print(abc329a(text))
