# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc321/tasks/abc321_b

import io
import sys

##########
_INPUT = """\
4 25
0 0 20
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc321b(target,scorelist):
    answer = -1
#    print(scorelist)

    scorelist_int = []
    for score in scorelist :
        scorelist_int.append(int(score))

    scorelist_int_sorted = sorted(scorelist_int)

    del scorelist_int_sorted[int(len(scorelist_int_sorted)-1)]

    if target - sum(scorelist_int_sorted) <= 0:
        answer = 0
        return answer

    del scorelist_int_sorted[0]
#    print(scorelist_int_sorted)

    diff = target - sum(scorelist_int_sorted)
#    print(sum(scorelist_int_sorted))

    if diff > 0:
        answer = diff

    if diff > 100:
        answer = -1

    if diff > max(scorelist_int):
        answer = -1

    return answer 

if __name__ == '__main__':
    list = input().split(" ")
    n_round = int(list[0])
    target = int(list[1])
    scorelist = input().split(" ")

    print(abc321b(target,scorelist))
