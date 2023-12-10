# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc332/tasks/abc332_c

import io
import sys
import math

##########
_INPUT = """\
3 1
222
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc332c(m,s):
    answer = 0
    max_logo_t_shirts = 0
    plain_t_shirts = 0
    logo_t_shirts = 0

#    print("m=",m)

    for i in range(len(s)):
        if s[i] == "0":
            if logo_t_shirts > max_logo_t_shirts:
                max_logo_t_shirts = logo_t_shirts
            plain_t_shirts = 0
            logo_t_shirts = 0
        elif s[i] == "1":
            if m > plain_t_shirts:
                plain_t_shirts += 1
            else:
                logo_t_shirts += 1
        elif s[i] == "2":
            logo_t_shirts += 1
#        print("plain_t_shirts=",plain_t_shirts,"logo_t_shirts=",logo_t_shirts)

    if logo_t_shirts > max_logo_t_shirts:
        max_logo_t_shirts = logo_t_shirts

#        print("max_logo_t_shirts=",max_logo_t_shirts)

    answer = max_logo_t_shirts

    return answer


if __name__ == '__main__':
    n,m = map(int,input().split())
    s = str(sys.stdin.readline().rstrip())

    print(abc332c(m,s))
