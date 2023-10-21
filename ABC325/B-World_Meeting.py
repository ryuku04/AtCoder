# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc325/tasks/abc325_b

import io
import sys

##########
_INPUT = """\
6
31 3
20 8
11 5
4 3
47 14
1 18
"""
sys.stdin = io.StringIO(_INPUT)
##########

def canAttend(time, timezone):
    localtime = int((time + timezone) % 24)
    if 9 <= localtime <= 17:
        return True
    
    return False


def abc325b(wlist,xlist):
    answer = 0
#    print(wlist)
#    print(xlist)

    for time in range(0, 24):
        attendee = 0
        for i in range(0, len(wlist)):
            if canAttend(int(time), int(xlist[i])) == True:
                attendee += int(wlist[i])
#        print(time,attendee)
        if attendee > answer:
            answer = attendee 

    return answer


if __name__ == '__main__':
    textline = []
    wlist = []
    xlist = []
    n = int(sys.stdin.readline().rstrip())
    for i in range(0,n):
        textline = sys.stdin.readline().rstrip().split(" ")
        wlist.append(textline[0])
        xlist.append(textline[1])

    print(abc325b(wlist,xlist))
