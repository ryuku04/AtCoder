# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc326/tasks/abc326_c

import io
import sys

##########
_INPUT = """\
8 6
2 3 5 7 11 13 17 19
"""
sys.stdin = io.StringIO(_INPUT)
##########

def find_max_index(lst, num):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return left - 1

def abc326c(m,alist):
    answer = 1
#    print(len(alist),m)
#    print(alist)

    alist_st = sorted(alist)
#    print(alist_st)

    for i in range(0,len(alist_st)):
        point = alist_st[i]
        x = find_max_index(alist_st, point+m)
        counter = x - i + 1
        if counter - answer > 0:
            answer = counter
#            print("i=",i,"alist[i]",point,"alist[i]+m",point+m)
#            print("x=",x)
#            print("counter=",counter)

    return answer


if __name__ == '__main__':
    alist = []
    m = int(sys.stdin.readline().rstrip().split(" ")[1])
    textline = sys.stdin.readline().rstrip().split(" ")
    for text in textline:
        alist.append(int(text))
    
    print(abc326c(m,alist))

