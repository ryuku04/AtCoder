# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc323/tasks/abc323_a

import io
import sys

##########
_INPUT = """\
1010100000101000
""
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc323a(text):
    answer = "Yes"

    for i in range(1,16,2):
        if int(text[i]) != 0:
#            print(i,text[i])
            answer = "No"

    return answer


if __name__ == '__main__':
    textline = input()

    print(abc323a(textline))
