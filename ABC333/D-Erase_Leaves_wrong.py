# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc333/tasks/abc333_d

import io
import sys
import math
import queue

##########
_INPUT = """\
9
1 2
2 3
2 4
2 5
1 6
6 7
7 8
7 9
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc333d(tree):
    answer = 0
    q = queue.Queue()

    print(tree)

    tree_in_1 = [t for t in tree if '1' in t]
    q.put(1)
    print(tree_in_1)

    if(len(tree_in_1) == 1):
        answer = 1
        return answer

    #tree_in_1から出発して、最短で葉までたどり着ける経路を計算してその回数を出力すればOK
    NotClearflg = True
    point = 1

    while(len(tree_in_p) != 1):
        point += tree_in_1[xxxx][1]
        point_str= str(point)

        tree_in_p = [t for t in tree if point_str in t]
        q.put(point)

        answer += 1


    return answer


if __name__ == '__main__':
    n = int(input())
    tree = []
    for i in range(n-1):
        un = sys.stdin.readline().rstrip().split(" ")
        tree.append(un)

    print(abc333d(tree))
