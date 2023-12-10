# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc332/tasks/abc332_a

import io
import sys

##########
_INPUT = """\
2 1600 500
1000 1
100 6
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc332a(s,k,plist,qlist):
    answer = 0

    for i in range(len(plist)):
        answer += plist[i]*qlist[i]

    if answer < s:
        answer += k
   
    return answer


if __name__ == '__main__':
    plist = []
    qlist = []
    n,s,k = map(int,input().split())
    for i in range(n):
        pq = sys.stdin.readline().rstrip().split(" ")
        plist.append(int(pq[0]))
        qlist.append(int(pq[1]))

    print(abc332a(s,k,plist,qlist))
