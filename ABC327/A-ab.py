# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc327/tasks/abc327_a

import io
import sys

##########
_INPUT = """\
3
abc
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc327a(s):
    answer = "Yes"

    if s.find('ba') == -1 and s.find('ab') == -1:
        answer = "No"

    return answer


if __name__ == '__main__':
    n = input()
    s = input()

    print(abc327a(s))
