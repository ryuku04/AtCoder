# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc327/tasks/abc327_b

import io
import sys

##########
_INPUT = """\
10000000000
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc327b(number):
    answer = -1

    i = 1
    while (i**i - number <= 0):
#        print("i=",i)
        if i**i - number == 0:
            answer = i
#            print("i**i=",i**i)
            break
        i += 1

    return answer


if __name__ == '__main__':
    number = int(sys.stdin.readline().rstrip())

    print(abc327b(number))
