# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc331/tasks/abc331_b

import io
import sys
import math

##########
_INPUT = """\
16 10 150 200
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc331b(n,s,m,l):
    answer = 99999999999
    max_num_s = math.ceil(n/6)
    max_num_m = math.ceil(n/8)
    max_num_l = math.ceil(n/12)

#    print("n=",n)
#    print("price_l=",l,"price=",m,"price_s=",s)

    for i in range(0,max_num_l+1):
        j = 0
        k = 0 
        num = 12*i + 8*j + 6*k
        if num >= n:
            price = l*i + m*j + s*k
            if price < answer:
                answer = price
#                print("num_l=",i,"num_m=",j,"num_s=",k,"price=",price)
        for j in range(0,max_num_m+1):
            k = 0 
            num = 12*i + 8*j + 6*k
            if num >= n :
                price = l*i + m*j + s*k
                if price < answer:
                    answer = price
#                    print("num_l=",i,"num_m=",j,"num_s=",k,"price=",price)

            k = math.ceil((n-12*i-8*j)/6)
            num = 12*i + 8*j + 6*k
            if num >= n and k >= 0:
                price = l*i + m*j + s*k
                if price < answer:
                    answer = price
#                    print("num_l=",i,"num_m=",j,"num_s=",k,"price=",price)

    return answer


if __name__ == '__main__':
    n,s,m,l = map(int,input().split())

    print(abc331b(n,s,m,l))
