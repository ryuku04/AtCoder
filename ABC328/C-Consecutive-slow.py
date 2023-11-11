# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc328/tasks/abc328_c

import io
import sys

##########
_INPUT = """\
5 1
aaaaa
1 5
"""
sys.stdin = io.StringIO(_INPUT)
##########

def count_consecutive_char(text):
    answer = 0
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            answer += 1

    return answer

def abc328c(s,llist,qlist):
    answerlist = []
    answer = ""

#    print(s)
#    print(llist)
#    print(qlist)

    for i in range(len(qlist)):
#        print("s=",s[int(llist[i])-1:int(qlist[i])])
        answerlist.append(str(count_consecutive_char(s[int(llist[i])-1:int(qlist[i])])))
   
    answer = "\n".join(answerlist)

    return answer


if __name__ == '__main__':

    n,q = map(int,input().split())
    s = sys.stdin.readline().rstrip()
    llist = []
    qlist = []
    for i in range(q):
        lq = sys.stdin.readline().rstrip().split(" ")
        llist.append(lq[0])
        qlist.append(lq[1])
    
    print(abc328c(s,llist,qlist))
