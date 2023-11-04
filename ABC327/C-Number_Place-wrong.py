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

def IsCoitain1to9(list):
    answer = False

    if ("1" in list)*("2" in list)*("3" in list)*("4" in list)*("5" in list) \
           *("6" in list)*("7" in list)*("8" in list)*("9" in list) == True:
        answer = True

    return answer

def getTransposeMatrix(aij):
    aij_t = []

    for i in range(len(aij)):
        tr_row = []
        for vector in aij:
            tr_row.append(vector[i])
        aij_t.append(tr_row)    
    
    return aij_t

def abc327c(aij):
    answer = "Yes"

#    for i in range(9):
#        print(aij[i])

    aij_t = getTransposeMatrix(aij)
#    print(aij_t)

#   row -check
    for i in range(9):
#        print("i=0","j=",j,"a1j=",aij[0][j])
        if IsCoitain1to9(aij[i]) == False:
            answer = "No"
#            print("Error in row-check i=",i)
            break

#   column-check
    for i in range(9):
#        print("i=0","j=",j,"a1j=",aij_t[0][j])
        if IsCoitain1to9(aij_t[i]) == False:
            answer = "No"
#            print("Error in column-check i=",i)
            break

#  3*3 matrix-check
    matrix = [0]*9
    for ik in range(3):
        for jk in range(3):
            for i in range(3):
                for j in range(3):
                    l = 3*i + j 
                    matrix[l] = aij[i+3*(ik-1)][j+3*jk]
#            print("ik=",ik,"jk=",jk,matrix)
        if IsCoitain1to9(matrix) == False:
                answer = "No"
#                print("Error in 3*3 matrix-check. ik=",ik,"ik=",jk,matrix)
                break

    return answer


if __name__ == '__main__':
    aij = []

    for i in range(9):
        aij.append(input().split(" "))
    
    print(abc327c(aij))

