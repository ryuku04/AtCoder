# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc319/tasks/abc319_c

import io
import sys
import itertools

##########
_INPUT = """\
7 7 6
8 6 8
7 7 6
"""
sys.stdin = io.StringIO(_INPUT)
# anser = 0.004982363315696649029982363316
##########

def DoGakkari(takahashilist):

    # row-check
    if takahashilist[0] != 0 and takahashilist[0] == takahashilist[1] and takahashilist[2] == 0:
        return True
    if takahashilist[1] != 0 and takahashilist[1] == takahashilist[2] and takahashilist[0] == 0:
        return True
    if takahashilist[2] != 0 and takahashilist[2] == takahashilist[0] and takahashilist[1] == 0:
        return True

    if takahashilist[3] != 0 and takahashilist[3] == takahashilist[4] and takahashilist[5] == 0:
        return True
    if takahashilist[4] != 0 and takahashilist[4] == takahashilist[5] and takahashilist[6] == 0:
        return True
    if takahashilist[5] != 0 and takahashilist[5] == takahashilist[3] and takahashilist[4] == 0:
        return True

    if takahashilist[6] != 0 and takahashilist[6] == takahashilist[7] and takahashilist[8] == 0:
        return True
    if takahashilist[7] != 0 and takahashilist[7] == takahashilist[8] and takahashilist[6] == 0:
        return True
    if takahashilist[8] != 0 and takahashilist[8] == takahashilist[6] and takahashilist[7] == 0:
        return True


    # column-check
    if takahashilist[0] != 0 and takahashilist[0] == takahashilist[3] and takahashilist[6] == 0:
        return True
    if takahashilist[3] != 0 and takahashilist[3] == takahashilist[6] and takahashilist[0] == 0:
        return True
    if takahashilist[6] != 0 and takahashilist[6] == takahashilist[0] and takahashilist[3] == 0:
        return True

    if takahashilist[1] != 0 and takahashilist[1] == takahashilist[4] and takahashilist[7] == 0:
        return True
    if takahashilist[4] != 0 and takahashilist[4] == takahashilist[7] and takahashilist[1] == 0:
        return True
    if takahashilist[7] != 0 and takahashilist[7] == takahashilist[1] and takahashilist[4] == 0:
        return True

    if takahashilist[2] != 0 and takahashilist[2] == takahashilist[5] and takahashilist[8] == 0:
        return True
    if takahashilist[5] != 0 and takahashilist[5] == takahashilist[8] and takahashilist[2] == 0:
        return True
    if takahashilist[8] != 0 and takahashilist[8] == takahashilist[2] and takahashilist[5] == 0:
        return True

    # diagonal-check
    if takahashilist[0] != 0 and takahashilist[0] == takahashilist[4] and takahashilist[8] == 0:
        return True
    if takahashilist[4] != 0 and takahashilist[4] == takahashilist[8] and takahashilist[0] == 0:
        return True
    if takahashilist[8] != 0 and takahashilist[8] == takahashilist[0] and takahashilist[4] == 0:
        return True

    if takahashilist[2] != 0 and takahashilist[2] == takahashilist[4] and takahashilist[6] == 0:
        return True
    if takahashilist[4] != 0 and takahashilist[4] == takahashilist[6] and takahashilist[2] == 0:
        return True
    if takahashilist[6] != 0 and takahashilist[6] == takahashilist[2] and takahashilist[4] == 0:
        return True


def abc319c(clist):
    answer = 0
    gakkari_counter = 0
    total_attempts = 9*8*7*6*5*4*3*2*1
    takahashilist = [0]*9
    n123456789 = [1,2,3,4,5,6,7,8,9]

#    print(clist)

    for num in itertools.permutations(n123456789, 9):
#        print(num)
#    for iii in range(1):
#        num = [4,7,3,1,5,6,2,8,9]
        takahashilist = [0]*9
        for i in range(1,9):
            takahashilist[num.index(i)] = clist[num.index(i)]
#            print("takahashilist=",takahashilist)
            if DoGakkari(takahashilist) == True:
                gakkari_counter += 1
                break

#    print("gakkari_counter=",gakkari_counter)
#    print("total_attempts",total_attempts)

    answer = (total_attempts-gakkari_counter)/total_attempts

    return answer 

if __name__ == '__main__':
    clist = []
    c0 = input().split(" ")
    c1 = input().split(" ")
    c2 = input().split(" ")

    for i in range(3):
        clist.append(c0[i])
    for i in range(3):
        clist.append(c1[i])
    for i in range(3):
        clist.append(c2[i])

    print(abc319c(clist))

