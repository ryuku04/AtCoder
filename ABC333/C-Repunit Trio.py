# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc333/tasks/abc333_c

import io
import sys
import math

##########
_INPUT = """\
333
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc333c(n):
    answer = 0
    Repunit1 = "1"
    Repunit2 = "1"
    Repunit3 = ""

    for i in range(n):
        if Repunit1 == Repunit2 and Repunit2 == Repunit3 and Repunit3 == Repunit1:
            Repunit1 += "1"
            Repunit2 = "1"
            Repunit3 = "1"
        elif Repunit2 == Repunit3 and Repunit1 != Repunit2:
            Repunit2 += "1"
            Repunit3 = "1"
        elif Repunit1 == Repunit2 and Repunit2 != Repunit3:
            Repunit3 += "1"
        elif Repunit1 != Repunit2 and Repunit2 != Repunit3:
            Repunit3 += "1"
#        sum = int(Repunit1) + int(Repunit2) + int(Repunit3)
#        print(i,Repunit1,Repunit2,Repunit3,sum)

    answer = int(Repunit1) + int(Repunit2) + int(Repunit3)

    return answer


if __name__ == '__main__':
    n = int(input())

    print(abc333c(n))
