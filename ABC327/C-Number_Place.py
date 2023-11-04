# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc327/tasks/abc327_c

import io
import sys

##########
_INPUT = """\
1 2 3 4 5 6 7 8 9
2 3 4 5 6 7 8 9 1
3 4 5 6 7 8 9 1 2
4 5 6 7 8 9 1 2 3
5 6 7 8 9 1 2 3 4
6 7 8 9 1 2 3 4 5
7 8 9 1 2 3 4 5 6
8 9 1 2 3 4 5 6 7
9 1 2 3 4 5 6 7 8
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc327c(aij):
    answer = "Yes"

#    for i in range(9):
#        print(aij[i])

    aij_t = []
    for i in range(9):
        tr_row = []
        for vector in aij:
            tr_row.append(vector[i])
        aij_t.append(tr_row)    
#    print(aij_t)

#   row -check
    for i in range(9):
#        print("i=0","j=",j,"a1j=",aij[0][j])
        if ("1" in aij[i])*("2" in aij[i])*("3" in aij[i])*("4" in aij[i])*("5" in aij[i]) \
           *("6" in aij[i])*("7" in aij[i])*("8" in aij[i])*("9" in aij[i]) == False:
            answer = "No"
#            print("Error in row-check i=",i)
            break

#   column-check
    for i in range(9):
#        print("i=0","j=",j,"a1j=",aij_t[0][j])
        if ("1" in aij_t[i])*("2" in aij_t[i])*("3" in aij_t[i])*("4" in aij_t[i])*("5" in aij_t[i]) \
           *("6" in aij_t[i])*("7" in aij_t[i])*("8" in aij_t[i])*("9" in aij_t[i]) == False:
            answer = "No"
#            print("Error in column-check i=",i)
            break

#  3*3 matrix-check
    matrix = [0]*9
    for k in range(3):
        for i in range(3):
            for j in range(3):
                l = 3*i + j 
                matrix[l] = aij[i][j+3*k]
#        print("i=1-3","k=",k,matrix)
        if ("1" in matrix)*("2" in matrix)*("3" in matrix)*("4" in matrix)*("5" in matrix) \
           *("6" in matrix)*("7" in matrix)*("8" in matrix)*("9" in matrix) == False:
            answer = "No"
#            print("Error in 3*3 matrix-check. i=1-3","k=",k,matrix)
            break

    for k in range(3):
        for i in range(3):
            for j in range(3):
                l = 3*i + j 
                matrix[l] = aij[i+3][j+3*k]
#        print("i=4-6","k=",k,matrix)
        if ("1" in matrix)*("2" in matrix)*("3" in matrix)*("4" in matrix)*("5" in matrix) \
           *("6" in matrix)*("7" in matrix)*("8" in matrix)*("9" in matrix) == False:
            answer = "No"
#            print("Error in 3*3 matrix-check. i=4-6","k=",k,matrix)
            break

    for k in range(3):
        for i in range(3):
            for j in range(3):
                l = 3*i + j 
                matrix[l] = aij[i+6][j+3*k]
#        print("i=7-9","k=",k,matrix)
        if ("1" in matrix)*("2" in matrix)*("3" in matrix)*("4" in matrix)*("5" in matrix) \
           *("6" in matrix)*("7" in matrix)*("8" in matrix)*("9" in matrix) == False:
            answer = "No"
#            print("Error in 3*3 matrix-check. i=7-9","k=",k,matrix)
            break


    return answer


if __name__ == '__main__':
    aij = []

    for i in range(9):
        aij.append(input().split(" "))
    
    print(abc327c(aij))

