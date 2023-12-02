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
    
    alist_sorted = sorted([(a, i) for i, a in enumerate(alist_int)], reverse=True)
#    print(alist_sorted)

    ans = 0
    dep_count = 0
    a_before = alist_sorted[0][0]
    for a,i in alist_sorted:
        dep_count += 1
        if a == a_before:
            blist.append((i,ans))
            a_before = a
            continue
        if dep_count == 1:
            ans += a_before
        else:
            ans += a_before*(dep_count-1)
        blist.append((i,ans))
        a_before = a
        dep_count = 1

#    print(blist)

    blist.sort()
    answerlist = [str(b) for i, b in blist]

#    print(answerlist)

    answer = " ".join(answerlist)

    return answer


if __name__ == '__main__':
    n = int(input())
    alist = sys.stdin.readline().rstrip().split(" ")

    print(abc331c(alist))
