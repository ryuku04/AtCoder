# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc320/tasks/abc322_b

import io
import sys

##########
_INPUT = """\
3 3
abc
abcabc
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc322b(n,m,string,text):
    answer = 3

    if text.find(string) == 0:
        answer = answer -2

    if text.rfind(string) == len(text)-len(string):
        answer = answer -1

#    print(text)
#    print(len(text))
#    print(string)
#    print(len(string))

    return answer 

if __name__ == '__main__':
    list = input().split(" ")
    n = list[0]
    m = list[1]
    string = input()
    text = input()

    print(abc322b(n,m,string,text))
