# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc319/tasks/abc319_c

import io
import sys
import itertools

##########
_INPUT = """\
3 1 9
2 5 6
2 7 1
"""
sys.stdin = io.StringIO(_INPUT)
##########

def DoGakkari(takahashilist):
    if takahashilist[0] == takahashilist[1]:
        return True
    if takahashilist[1] == takahashilist[2]:
        return True
    if takahashilist[2] == takahashilist[0]:
        return True

    if takahashilist[3] == takahashilist[4]:
        return True
    if takahashilist[4] == takahashilist[5]:
        return True
    if takahashilist[5] == takahashilist[3]:
        return True

    if takahashilist[6] == takahashilist[7]:
        return True
    if takahashilist[7] == takahashilist[8]:
        return True
    if takahashilist[8] == takahashilist[6]:
        return True

    if takahashilist[0] == takahashilist[3]:
        return True
    if takahashilist[3] == takahashilist[6]:
        return True
    if takahashilist[6] == takahashilist[0]:
        return True

    if takahashilist[1] == takahashilist[4]:
        return True
    if takahashilist[4] == takahashilist[7]:
        return True
    if takahashilist[7] == takahashilist[1]:
        return True

    if takahashilist[2] == takahashilist[5]:
        return True
    if takahashilist[5] == takahashilist[8]:
        return True
    if takahashilist[8] == takahashilist[2]:
        return True

    if takahashilist[0] == takahashilist[4]:
        return True
    if takahashilist[4] == takahashilist[8]:
        return True
    if takahashilist[8] == takahashilist[0]:
        return True

    if takahashilist[2] == takahashilist[4]:
        return True
    if takahashilist[4] == takahashilist[7]:
        return True
    if takahashilist[7] == takahashilist[2]:
        return True




def abc319c(clist):
    answer = 0
    total_attempts = 9*8*7*6*5*4*3*2*1
    gakkari_counter = 0

    print("---clist---")
    print(clist[0],clist[1],clist[2])
    print(clist[3],clist[4],clist[5])
    print(clist[6],clist[7],clist[8])
    print("----------")

    takahashilist = [""]*9
    takahashilist[0] = clist[0]
    takahashilist[3] = clist[3]
    takahashilist[6] = clist[6]

    print("---takahashilist---")
    print(takahashilist[0],takahashilist[1],takahashilist[2])
    print(takahashilist[3],takahashilist[4],takahashilist[5])
    print(takahashilist[6],takahashilist[7],takahashilist[8])
    print("----------")

    print(DoGakkari(takahashilist))

    n123456789 = [1,2,3,4,5,6,7,8,9]

    for num in itertools.permutations(n123456789, 9):
        print(num)
        for i in range(9):
            print(num[i])
        if int(num[3]) > 6:
            break


    if DoGakkari(takahashilist) == True:
        gakkari_counter += 1

    answer = gakkari_counter/total_attempts

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

