# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc332/tasks/abc332_d

import io
import sys
import math

##########
_INPUT = """\
5 5
710511029 136397527 763027379 644706927 447672230
979861204 57882493 442931589 951053644 152300688
43971370 126515475 962139996 541282303 834022578
312523039 506696497 664922712 414720753 304621362
325269832 191410838 286751784 732741849 806602693
806602693 732741849 286751784 191410838 325269832
304621362 414720753 664922712 506696497 312523039
834022578 541282303 962139996 126515475 43971370
152300688 951053644 442931589 57882493 979861204
447672230 644706927 763027379 136397527 710511029
"""
sys.stdin = io.StringIO(_INPUT)
##########

def replace_h_element(i,j,mtx):
    tmp = mtx[i+1][j]
    mtx[i+1][j] = mtx[i][j]
    mtx[i][j] = tmp
    return mtx

def replace_w_element(i,j,mtx):
    tmp = mtx[i][j+1]
    mtx[i][j+1] = mtx[i][j]
    mtx[i][j] = tmp
    return mtx

def abc332d(mtx_a,mtx_b):
    answer = -1
    print("A=",mtx_a)
    print("B=",mtx_b)

    mtx_a_1d = sum(mtx_a, [])
    mtx_a_1d.sort()
    mtx_b_1d = sum(mtx_b, [])
    mtx_b_1d.sort()

    print("A'=",mtx_a_1d)
    print("B'=",mtx_b_1d)

    if mtx_a_1d != mtx_b_1d:
        return answer
    
    i = 0
#    while(mtx_a == mtx_b):
#        i+=1


    answer = i

    return answer


if __name__ == '__main__':
    textline = []
    mtx_a = []
    mtx_b = []

    h,w = map(int,input().split())
    for i in range(h):
        textline = sys.stdin.readline().rstrip().split(" ")
        mtx_a.append(textline)
    for i in range(h):
        textline = sys.stdin.readline().rstrip().split(" ")
        mtx_b.append(textline)

    print(abc332d(mtx_a,mtx_b))
