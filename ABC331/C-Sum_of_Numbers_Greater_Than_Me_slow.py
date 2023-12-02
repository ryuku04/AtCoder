# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc331/tasks/abc331_c

import io
import sys
import math

##########
_INPUT = """\
10
31 42 53 23 53 58 97 93 23 54
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc331c(alist):
    answerlist = []
    blist = []

    alist_int = []
    for i in range(len(alist)):
        alist_int.append(int(alist[i]))
#    print(alist_int)
    
    alist_sorted = sorted(alist_int, reverse=True)
#    print(alist_sorted)

    ans = 0
    dep_count = 0
    a_before = alist_sorted[0]
    for a in alist_sorted:
        dep_count += 1
        if a == a_before:
            blist.append(ans)
            a_before = a
            continue
        if dep_count == 1:
            ans += a_before
        else:
            ans += a_before*(dep_count-1)
        blist.append(ans)
        a_before = a
        dep_count = 1

#    print(blist)

    for a in alist:
        idx = alist_sorted.index(int(a))
        answerlist.append(str(blist[idx]))

#    print(answerlist)

    answer = " ".join(answerlist)

    return answer


if __name__ == '__main__':
    n = int(input())
    alist = sys.stdin.readline().rstrip().split(" ")

    print(abc331c(alist))
