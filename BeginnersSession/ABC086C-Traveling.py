# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abs/tasks/arc089_a

import io
import sys

##########
_INPUT = """\
2
5 1 1
100 1 1
"""
sys.stdin = io.StringIO(_INPUT)
##########

def ABC086C(num,list):
    answer = "Yes"
    tt = 0
    xt = 0
    yt = 0
   
    for data in list:
        t = int(data.split(" ")[0])
        x = int(data.split(" ")[1])
        y = int(data.split(" ")[2])

        xylen = abs(x-xt) + abs(y-yt)

        if((t-tt-xylen) < 0 or (t-tt-xylen)%2 == 1):
            print("---")
            print(tt,xt,yt)
            print(t,x,y)
            print("---")
            answer = "No"
            break

        tt = t
        xt = x
        yt = y

    return answer 

if __name__ == '__main__':
    list = []
    num = int(input())
    for i in range(0,num):
        list.append(input())

    print(ABC086C(num,list))
