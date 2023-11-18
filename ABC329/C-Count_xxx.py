# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc329/tasks/abc329_c

import io
import sys
import string

##########
_INPUT = """\
6
aaabaa
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc329c(text):
    answer = 0
    answerlist = list()

    for abc in list(string.ascii_lowercase):
        answerlist.append([abc, 0])

    i = 0
    tlen = 1
    while i < len(text)-1:
        if text[i] != text[i+1]:
            for j in range(len(answerlist)):
                if text[i] == answerlist[j][0]:
                    if answerlist[j][1] < tlen:
                        answerlist[j][1] = tlen
#                        print(answerlist[j])
                continue
            tlen = 0
        i += 1
        tlen += 1

    for j in range(len(answerlist)):
        if text[i-1] == answerlist[j][0]:
            if answerlist[j][1] < tlen:
                answerlist[j][1] = tlen
#                print(answerlist[j])
 
#    print(answerlist)

    for ans in answerlist:
        answer += ans[1]

    return answer


if __name__ == '__main__':
    n = sys.stdin.readline().rstrip()
    s = sys.stdin.readline().rstrip()
    
    print(abc329c(s))
