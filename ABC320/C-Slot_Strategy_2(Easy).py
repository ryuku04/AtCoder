# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc320/tasks/abc320_c

import io
import sys

##########
_INPUT = """\
10
1937458062
8124690357
2385760149
"""
sys.stdin = io.StringIO(_INPUT)
##########

def check_duplicates(list1, list2, list3):
    ans = []

    for i in range(0, len(list1)):
        if (list1[i] in list2) == True and (list1[i] in list3) == True:
            ans.append(list1[i])

    if len(ans) == 0:
        return False
    
    return list(set(ans))

def abc320c(m,slot1,slot2,slot3):
    answer= int(3*m)
    m_i= int(m)

    list1 = list(slot1)
    list2 = list(slot2)
    list3 = list(slot3)

#    print(m)
#    print(list1)
#    print(list2)
#    print(list3)

    slist = check_duplicates(list1, list2, list3)

    if slist == False:
        return -1

    for i in range(3*m_i):
        for j in range(3*m_i):
            for k in range(3*m_i):
                if i != j and j != k and k != i and \
                    list1[i%m_i] == list2[j%m_i] == list3[k%m_i]:
                    ans_tmp = max(i,j,k)
                    if(ans_tmp < answer):
                        answer = ans_tmp
#                        print(ans_tmp, i,j,k)

    return answer 

if __name__ == '__main__':
    m = input()
    slot1 = str(input())
    slot2 = str(input())
    slot3 = str(input())

    print(abc320c(m,slot1,slot2,slot3))

