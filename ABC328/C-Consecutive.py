# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc328/tasks/abc328_c

import io
import sys

##########
_INPUT = """\
11 4
mississippi
3 9
4 10
4 6
7 7
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc328c(s,lqlist):
    slist = ["0"]
    answerlist = []
    answer = ""

#    print(s)
#    print(lqlist)

    counter = 0 
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            counter += 1
        slist.append(str(counter))

#    print(slist)

    for i in range(len(lqlist)):
#        print("s[q]=",slist[int(lqlist[i][1])-1],"s[l]=",slist[int(lqlist[i][0])-1])
        ans = int(slist[int(lqlist[i][1])-1]) - int(slist[int(lqlist[i][0])-1])
        answerlist.append(str(ans))
   
    answer = "\n".join(answerlist)

    return answer


if __name__ == '__main__':
    n,q = map(int,input().split())
    s = sys.stdin.readline().rstrip()
    lqlist = []

    for row in range(q):
        row = list(map(int, sys.stdin.readline().rstrip().split()))
        lqlist.append(row)
    
    print(abc328c(s,lqlist))
