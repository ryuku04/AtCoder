# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc328/tasks/abc328_b

import io
import sys

##########
_INPUT = """\
9
1 2 3 4 5 6 7 8 99
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc328b(monthdaylist):
    answer = 0

    month = 1
    for monthday in monthdaylist:
        for i in range(1,int(monthday)+1):
            i10 = int(i/10)
            i1 =  int(i%10)
            month10 = int(month/10)
            month1 = int(month%10)
            if i < 10:
                i10 = i1
            if month < 10:
                month10 = month1
            if month1 == month10 and month10 == i1 and i1 == i10:
#                print("month=",month,"i=",i)
                answer += 1
        month += 1

    return answer


if __name__ == '__main__':
    n = sys.stdin.readline().rstrip()
    monthdaylist = sys.stdin.readline().rstrip().split(" ")

    print(abc328b(monthdaylist))
