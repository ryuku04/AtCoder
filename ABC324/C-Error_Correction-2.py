# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc324/tasks/abc324_c

import io
import sys

##########
_INPUT = """\
9 atcoder
atoder
atcode
athqcoder
atcoder
tacoder
jttcoder
atoder
atceoder
atcoer
"""
sys.stdin = io.StringIO(_INPUT)
##########

def IsSameOr1LetterDifferent(receivedtext, text):
    if receivedtext == text:
#        print(receivedtext,text)
        return True

    if len(receivedtext)-len(text) == 0:
        for j in range(0,len(receivedtext)):
            if receivedtext[j] != text[j]:
#                print(longtext[j:],shorttext[j:])
                if receivedtext[j+1:] == text[j+1:]:
                    return True
                else:
                    return False

def Is1LetterInsertedOrDeleted(receivedtext, text):
    if len(receivedtext)-len(text) >= 0:
        longtext = receivedtext
        shorttext = text
    else:
        longtext = text
        shorttext = receivedtext

    if longtext[:len(longtext)-1] == shorttext:
#        print(longtext,shorttext)
        return True
    
    for j in range(0,len(shorttext)):
        if longtext[j] != shorttext[j]:
#           print(longtext[j+1:],shorttext[j:])
            if longtext[j+1:] == shorttext[j:]:
                return True
            else:
                return False


def abc324c(receivedtext,textlist):
#    print(receivedtext)
#    print(textlist)

    answerlist = []

    for i in range(0,len(textlist)):
        if abs(len(receivedtext)-len(textlist[i])) > 1 :
            continue
        if IsSameOr1LetterDifferent(receivedtext, textlist[i]) == True:
#            print(i+1,textlist[i],"IsSameOr1LetterDifferent")
            answerlist.append(i+1)
            continue
        if Is1LetterInsertedOrDeleted(receivedtext, textlist[i]) == True:
#            print(i+1,textlist[i],"Is1LetterInsertedOrDeleted")
            answerlist.append(i+1)
            continue
   
    return answerlist


if __name__ == '__main__':
    textlist = []
    textline = sys.stdin.readline().rstrip().split(" ")
    n = int(textline[0])
    receivedtext = textline[1]
    for i in range(0,n):
        textlist.append(str(sys.stdin.readline().rstrip()))
        
    answerlist = abc324c(receivedtext,textlist)

    print(len(answerlist))
    print(*answerlist)
