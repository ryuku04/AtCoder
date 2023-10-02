# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abs/tasks/abc085_c

import io
import sys

##########
_INPUT = """\
1000 1234000
"""
sys.stdin = io.StringIO(_INPUT)
##########

def ABC085C(num,money):
    for i in range(0,num+1):
        for j in range(0,num+1-i):
            money_t = 10000*(num-j-i) + 5000*j + 1000*i
            if money == money_t:
                answer = str(num-j-i) + " " + str(j) + " " + str(i)
                return answer

    return "-1 -1 -1"

if __name__ == '__main__':
    textline = input()
    num = int(textline.split(" ")[0])
    money = int(textline.split(" ")[1])

    print(ABC085C(num,money))
