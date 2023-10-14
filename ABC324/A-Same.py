# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc324/tasks/abc324_a

import io
import sys

##########
_INPUT = """\
10
73 8 55 26 97 48 37 47 35 55
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc324a(intlist):
    answer = "No"

    NotDuplicatesList = set(intlist)
#    print(NotDuplicatesList)
    if len(NotDuplicatesList) == 1:
        answer = "Yes"

    return answer


if __name__ == '__main__':
    n = input()
    intlist = input().split(" ")

    print(abc324a(intlist))
