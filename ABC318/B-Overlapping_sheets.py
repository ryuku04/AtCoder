# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc318/tasks/abc318_b

import io
import sys

##########
_INPUT = """\
3
0 1 0 1
0 3 0 5
5 10 0 10
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc318b(squarelist):
    answer = 0
    answerlist = [[0]*100 for i in range(100)]

#    print(squarelist)

    for square in squarelist:
        xs=square[0]
        xe=square[1]
        ys=square[2]
        ye=square[3]
#        print("xs=","xes=",xs,xe,"ys=","ye=",ys,ye)
        for xi in range(xs,xe):
            for yi in range(ys,ye):
                answerlist[xi][yi] = 1
#                print("xi=","yi=",xi,yi)
    
#    print(answerlist)

    answer = sum(sum(answerlist, []))

    return answer


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    squarelist= list()

    for row in range(n):
        row = list(map(int, sys.stdin.readline().rstrip().split(" ")))
        squarelist.append(row)

    print(abc318b(squarelist))
