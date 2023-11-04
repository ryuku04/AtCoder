# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc319/tasks/abc319_a

import io
import sys

##########
_INPUT = """\
semiexp
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc319a(username):

    ratingdict = {"tourist":3858,"ksun48":3679,"Benq":3658,"Um_nik":3648,"apiad":3638,"Stonefeang":3630,"ecnerwala":3613,"mnbvmar":3555,"newbiedmy":3516,"semiexp":3481}
    answer = ratingdict[username]
    
    return answer 

if __name__ == '__main__':
    username = input()

    print(abc319a(username))
