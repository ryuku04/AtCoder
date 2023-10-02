# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abs/tasks/abc087_b

##########
import io
import sys

_INPUT = """\
30
40
50
6000
"""
sys.stdin = io.StringIO(_INPUT)
##########

def ABC087B(num500,num100,num50,money):
    answer=0
   
    for i in range(0,num500+1):
        for j in range(0,num100+1):
            for k in range(0,num50+1):
                 money_t = 500*i + 100*j + 50*k
                 if money == money_t:
                      answer += 1
    return answer

if __name__ == '__main__':
    num500  = int(input())
    num100  = int(input())
    num50  = int(input())
    money  = int(input())

    print(ABC087B(num500,num100,num50,money))
