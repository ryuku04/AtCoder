# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc320/tasks/abc320_b

import io
import sys

##########
_INPUT = """\
AAAAAAAAAA
"""
sys.stdin = io.StringIO(_INPUT)
##########

def isPalindrome(text):
    result = True
    textlenght = len(text)
    
    for i in range(0, int(textlenght/2)):
        if str(text[i]) != str(text[textlenght-1-i]):
            result = False

    return result

def abc320b(text):
    answer = 1

    for i in range(2, len(text)+1):
        for j in range(0,len(text)+1-i):
#            print(i,j)
#            print(text[j:j+i])
            if (isPalindrome(text[j:j+i]) == True):
                answer = i
#                print(text[j:j+i])

    return answer 

if __name__ == '__main__':
    textline = input()

    print(abc320b(textline))
