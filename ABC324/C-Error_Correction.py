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

def IsSame(text1, text2):
    if text1 == text2:
        return True
    return False

def Is1LetterDifferent(receivedtext, text):
    if len(receivedtext) - len(text) == 0:
        for i in range(0,len(receivedtext)):
            if receivedtext[i] != text[i]:
#                print(longtext[i:],shorttext[i:])
                if receivedtext[i+1:] == text[i+1:]:
                    return True
                else:
                    return False

    return False

def Is1LetterInsertedOrDeleted(receivedtext, text):
    if abs(len(receivedtext) - len(text)) == 1:

        if len(receivedtext) - len(text) > 0:
            longtext = receivedtext
            shorttext = text
        else:
            longtext = text
            shorttext = receivedtext

        if longtext[:len(longtext)-1] == shorttext:
#            print(longtext,shorttext)
            return True
    
        for i in range(0,len(shorttext)):
            if longtext[i] != shorttext[i]:
#               print(longtext[i+1:],shorttext[i:])
                if longtext[i+1:] == shorttext[i:]:
                    return True
                else:
                    return False

    return False

def abc324c(receivedtext,textlist):
#    print(receivedtext)
#    print(textlist)

    answerlist = []

    for i in range(0,len(textlist)):
        if abs(len(receivedtext)-len(textlist[i])) > 1 :
            continue
        if IsSame(receivedtext, textlist[i]) == True:
#            print(i+1,textlist[i],"IsSame")
            answerlist.append(str(i+1))
            continue
        if Is1LetterDifferent(receivedtext, textlist[i]) == True:
#            print(i+1,textlist[i],"Is1LetterDifferent")
            answerlist.append(str(i+1))
            continue
        if Is1LetterInsertedOrDeleted(receivedtext, textlist[i]) == True:
#            print(i+1,textlist[i],"Is1LetterInsertedOrDeleted")
            answerlist.append(str(i+1))
            continue
   
    answer = str(len(answerlist)) + "\n" + " ".join(answerlist)
    
    return answer


if __name__ == '__main__':
    textlist = []
    textline = sys.stdin.readline().rstrip().split(" ")
    n = int(textline[0])
    receivedtext = textline[1]
    for i in range(0,n):
        textlist.append(str(sys.stdin.readline().rstrip()))
        
    print(abc324c(receivedtext,textlist))

