# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc328/tasks/abc328_a

import io
import sys

##########
_INPUT = """\
8 675
675 675 675 675 675 675 675 675
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc328a(x,scorelist):
    answer = 0

    for score in scorelist:
        if int(score) <= x:
            answer += int(score)

    return answer


if __name__ == '__main__':
    x = int(sys.stdin.readline().rstrip().split(" ")[1])
    scorelist = sys.stdin.readline().rstrip().split(" ")

    print(abc328a(x,scorelist))
