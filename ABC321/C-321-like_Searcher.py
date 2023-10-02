# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc321/tasks/abc321_c

import io
import sys

##########
_INPUT = """\
777
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc321c(n):
    anslist=[]

    ans = ""
    for i1 in range(9,0,-1):
        ans1 = ans
        ans1 = ans1 + str(i1)
        anslist.append(int(ans1))
        for i2 in range(i1-1,-1,-1):
            ans2 = ans1
            ans2 = ans2 + str(i2)
            anslist.append(int(ans2))
            for i3 in range(i2-1,-1,-1):
                ans3 = ans2
                ans3 = ans3 + str(i3)
                anslist.append(int(ans3))
                for i4 in range(i3-1,-1,-1):
                    ans4 = ans3
                    ans4 = ans4 + str(i4)
                    anslist.append(int(ans4))
                    for i5 in range(i4-1,-1,-1):
                        ans5 = ans4
                        ans5 = ans5 + str(i5)
                        anslist.append(int(ans5))
                        for i6 in range(i5-1,-1,-1):
                            ans6 = ans5
                            ans6 = ans6 + str(i6)
                            anslist.append(int(ans6))
                            for i7 in range(i6-1,-1,-1):
                                ans7 = ans6
                                ans7 = ans7 + str(i7)
                                anslist.append(int(ans7))
                                for i8 in range(i7-1,-1,-1):
                                    ans8 = ans7
                                    ans8 = ans8 + str(i8)
                                    anslist.append(int(ans8))
                                    for i9 in range(i8-1,-1,-1):
                                        ans9 = ans8
                                        ans9 = ans9 + str(i9)
                                        anslist.append(int(ans9))
                                        for i10 in range(i9-1,-1,-1):
                                            ans10 = ans9
                                            ans10 = ans10 + str(i10)
                                            anslist.append(int(ans10))
   
    anslist.sort()
#    print(anslist)
#    print(len(anslist))
    answer = anslist[n-1]

    return answer


if __name__ == '__main__':
    n = int(input())

    print(abc321c(n))
