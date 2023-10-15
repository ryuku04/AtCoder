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

def IsSame(receivedtext, text):
    if receivedtext == text:
         return True
    else:
         return False

def Is1LetterInserted(receivedtext, text):
    for i in range(1,len(text)+1):
        deletedtext = text[:i-1]+text[i:]
#        print(deletedtext)
        if receivedtext == deletedtext:
             return True

    return False

def Is1LetterDeleted(receivedtext, text):
    for i in range(1,len(receivedtext)+1):
        deletedtext = receivedtext[:i-1]+receivedtext[i:]
#        print(deletedtext)
        if text == deletedtext:
             return True

    return False
        
def Is1LetterChanged(receivedtext, text):
    if len(receivedtext) != len(text):
        return False

    for i in range(1,len(text)+1):
        deletedreceivedtext = text[:i-1]+text[i:]
        deletedtext = receivedtext[:i-1]+receivedtext[i:]
#        print(deletedtext,deletedreceivedtext)
        if deletedtext == deletedreceivedtext:
             return True

    return False

def abc324c(receivedtext,textlist):
#    print(receivedtext)
#    print(textlist)

    answer = ""
    answerlist = []

    for i in range(0,len(textlist)):
        if abs(len(receivedtext)-len(textlist[i])) > 1 :
            continue

        if IsSame(receivedtext, textlist[i]) == True:
            answerlist.append(str(i+1))
#            print(i+1,textlist[i],"IsSame")
            continue
        if Is1LetterInserted(receivedtext, textlist[i]) == True:
            answerlist.append(str(i+1))
#            print(i+1,textlist[i],"Is1LetterInserted")
            continue
        if Is1LetterDeleted(receivedtext, textlist[i]) == True:
            answerlist.append(str(i+1))
#            print(i+1,textlist[i],"Is1LetterDeleted")
            continue
        if Is1LetterChanged(receivedtext, textlist[i]) == True:
            answerlist.append(str(i+1))
#            print(i+1,textlist[i],"Is1LetterChanged")
            continue

    answer = str(len(answerlist)) + "\n"
    for ans in answerlist:
        answer = answer + ans + " " 
    if len(answerlist) != 0:
        answer.rstrip(" ")



    return answer


if __name__ == '__main__':
    textlist = []
    textline = input().split(" ")
    n = int(textline[0])
    receivedtext = textline[1]
    for i in range(0,n):
        textlist.append(str(input()))
        
    print(abc324c(receivedtext,textlist))
