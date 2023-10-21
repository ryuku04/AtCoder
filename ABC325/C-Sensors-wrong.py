# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc325/tasks/abc325_c

import io
import sys

##########
_INPUT = """\
5 47
.#..#..#####..#...#..#####..#...#...###...#####
.#.#...#.......#.#...#......##..#..#...#..#....
.##....#####....#....#####..#.#.#..#......#####
.#.#...#........#....#......#..##..#...#..#....
.#..#..#####....#....#####..#...#...###...#####
"""
sys.stdin = io.StringIO(_INPUT)
##########

def replaceCharAtIndext(char,index,text):
    new_text = text[:index] + char + text[index+1:]
    return new_text

'''
def seachLinkageSensor(i,j,hwlist,integratedhwlist):
#    print(i+1,j+1)
#    print(hwlist)
    answer = True
    if j != len(hwlist)-1:
        if hwlist[j+1][i] == "#":
            answer =  False
            integratedhwlist[j+1] = replaceCharAtIndext(".",i,integratedhwlist[j+1])
    if i != len(hwlist[j])-1:
        if hwlist[j][i+1] == "#":
            answer =  False
            integratedhwlist[j] = replaceCharAtIndext(".",i+1,integratedhwlist[j])
    if j != 0:
        if hwlist[j-1][i] == "#": 
            answer =  False
    if i != 0:
        if hwlist[j][i-1] == "#": 
            answer =  False
    if j != 0 and i != 0:
        if hwlist[j-1][i-1] == "#": 
            answer =  False
    if j != len(hwlist)-1 and i != 0:
        if hwlist[j+1][i-1] == "#":
            answer =  False
            integratedhwlist[j+1] = replaceCharAtIndext(".",i-1,integratedhwlist[j+1])
    if j != 0 and i != len(hwlist[j])-1:
        if hwlist[j-1][i+1] == "#": 
            answer =  False
            integratedhwlist[j-1] = replaceCharAtIndext(".",i+1,integratedhwlist[j-1])
    if j != len(hwlist)-1 and i != len(hwlist[j])-1:
        if hwlist[j+1][i+1] == "#":
            answer =  False
            integratedhwlist[j+1] = replaceCharAtIndext(".",i+1,integratedhwlist[j+1])

#    print(i+1,j+1,"The sensor is isorated")
    return answer
'''

def isLincagedSensor(i,j,hwlist):
    answer = False

    if j != len(hwlist)-1:
        if hwlist[j+1][i] == "#":
            return True
    if i != len(hwlist[j])-1:
        if hwlist[j][i+1] == "#":
            return True
    if j != 0:
        if hwlist[j-1][i] == "#": 
            return True
    if i != 0:
        if hwlist[j][i-1] == "#": 
            return True
    if j != 0 and i != 0:
        if hwlist[j-1][i-1] == "#": 
            return True
    if j != len(hwlist)-1 and i != 0:
        if hwlist[j+1][i-1] == "#":
            return True
    if j != 0 and i != len(hwlist[j])-1:
        if hwlist[j-1][i+1] == "#": 
            return True
    if j != len(hwlist)-1 and i != len(hwlist[j])-1:
        if hwlist[j+1][i+1] == "#":
            return True

    return answer

def integratedLinkageSensors(i,j,integratedhwlist):

    if j != len(integratedhwlist)-1:
        integratedhwlist[j+1] = replaceCharAtIndext(".",i,integratedhwlist[j+1])
    if i != len(integratedhwlist[j])-1:
        integratedhwlist[j] = replaceCharAtIndext(".",i+1,integratedhwlist[j])
    if j != len(integratedhwlist)-1 and i != 0:
        integratedhwlist[j+1] = replaceCharAtIndext(".",i-1,integratedhwlist[j+1])
    if j != 0 and i != len(integratedhwlist[j])-1:
        integratedhwlist[j-1] = replaceCharAtIndext(".",i+1,integratedhwlist[j-1])
    if j != len(integratedhwlist)-1 and i != len(integratedhwlist[j])-1:
        integratedhwlist[j+1] = replaceCharAtIndext(".",i+1,integratedhwlist[j+1])

    return integratedhwlist


def abc325c(hwlist):
    answer = 0
    integratedhwlist = hwlist.copy()

# check the sensor is Lincaged. If the sensor is Lincaged, integrated lincaged sensorlist[integratedhwlist].
    for j in range(len(hwlist)):
        for i in range(len(hwlist[j])):
            if hwlist[j][i] == "#":
#                print(i+1,j+1, "Sensor is deployed")
                if isLincagedSensor(i,j,hwlist) == True:
#                    print(i+1,j+1, "Sensor is lincaged")
                    integratedLinkageSensors(i,j,integratedhwlist)

#    print(hwlist)
#    print(integratedhwlist)

    for hw in integratedhwlist:
        answer += hw.count("#")

    return answer


if __name__ == '__main__':
    textline = []
    hwlist = []
    n = int(sys.stdin.readline().rstrip().split(" ")[0])
    for i in range(0,n):
        textline = sys.stdin.readline().rstrip().split(" ")
        hwlist.append(textline[0])

#    print(hwlist)
        
    print(abc325c(hwlist))

