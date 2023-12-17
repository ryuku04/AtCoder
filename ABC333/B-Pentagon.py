# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc333/tasks/abc333_b

import io
import sys

##########
_INPUT = """\
BD
BD
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc333b(s,t):
    answer = "No"

    s.sort()
    t.sort()
    s1s2 = "".join(s)
    t1t2 = "".join(t)

    if s1s2 == "AB" or s1s2 == "BC" or s1s2 == "CD" or s1s2 == "DE" or s1s2 == "AE":
        s1s2_len = 1
    elif s1s2 == "AC" or s1s2 == "BD" or s1s2 == "CE" or s1s2 == "AD" or s1s2 == "BE":
        s1s2_len = 1.6

    if t1t2 == "AB" or t1t2 == "BC" or t1t2 == "CD" or t1t2 == "DE" or t1t2 == "AE":
        t1t2_len = 1
    elif t1t2 == "AC" or t1t2 == "BD" or t1t2 == "CE" or t1t2 == "AD" or t1t2 == "BE":
        t1t2_len = 1.6

#    print(s1s2,s1s2_len)
#    print(t1t2,t1t2_len)

    if s1s2_len == t1t2_len:
        answer = "Yes"

    return answer


if __name__ == '__main__':
    s = list(input())
    t = list(input())

    print(abc333b(s,t))
