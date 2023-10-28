# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc326/tasks/abc326_b

import io
import sys

##########
_INPUT = """\
516
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc326b(n):
    answer = 919

    for number in range(n, 919):
        number_str = str(number)
        if int(number_str[0])*int(number_str[1])-int(number_str[2]) == 0:
            answer = number_str
            break

    return answer


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())

    print(abc326b(n))
