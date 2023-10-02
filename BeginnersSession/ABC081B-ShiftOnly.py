# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abs/tasks/abc081_b

##########
import io
import sys

_INPUT = """\
4
5 6 8 10
"""
sys.stdin = io.StringIO(_INPUT)
##########

def ABC081B(inputtest1,inputtest2):

    answer = 0
    n = int(inputtest1)
    numlist_str = inputtest2.split(" ")
    numlist = list(map(int, numlist_str))
    flg = False

    while(True):
        for i in range(n):
            if numlist[i]%2 == 1:
                flg = True
                break
            else:
                numlist[i] = numlist[i]/2
        if flg == True:
            break
        answer = answer + 1
    return answer

if __name__ == '__main__':
    inputtest1  = str(input())
    inputtest2  = str(input())

    print(ABC081B(inputtest1,inputtest2))
