# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc326/tasks/abc326_c

import io
import sys

##########
_INPUT = """\
10 2
2 4 6 8 10 12 14 16 18 19
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc326c(m,alist):
    answer = 1
#    print(len(alist),m)
#    print(alist)

    alist_st = sorted(alist)
#    print(alist_st)

    for i in range(0,len(alist_st)):
        start_range = alist_st[i]
        end_range = alist_st[i] + m
        counter = 0
        for j in range(0,len(alist_st)):
            point = alist_st[j]
            if point- start_range >= 0 and end_range-point > 0:
                counter += 1
            elif point - start_range < 0:
                continue
            elif end_range - point <= 0:
                if counter - answer > 0:
                    answer = counter
#                    print(start_range,end_range,answer)
                break
        if counter - answer > 0:
            answer = counter
#            print(start_range,end_range,answer)

    return answer


if __name__ == '__main__':
    alist = []
    m = int(sys.stdin.readline().rstrip().split(" ")[1])
    textline = sys.stdin.readline().rstrip().split(" ")
    for text in textline:
        alist.append(int(text))

    print(abc326c(m,alist))

