# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abs/tasks/arc065_a

import io
import sys

##########
_INPUT = """\
erasedream
"""
sys.stdin = io.StringIO(_INPUT)
##########

def ABC049C(text):
    answer = "NO"
    text_cut = text
   
    while(len(text_cut) != 0):
        if text_cut.endswith("dreamer"):
            text_cut = text_cut.removesuffix("dreamer")
        elif text_cut.endswith("eraser"):
            text_cut = text_cut.removesuffix("eraser")
        elif text_cut.endswith("dream"):
            text_cut = text_cut.removesuffix("dream")
        elif text_cut.endswith("erase"):
            text_cut = text_cut.removesuffix("erase")
        else:
            return "NO"

    if len(text_cut) == 0:
        answer = "YES"   

    return answer 

if __name__ == '__main__':
    text  = str(input())

    print(ABC049C(text))
