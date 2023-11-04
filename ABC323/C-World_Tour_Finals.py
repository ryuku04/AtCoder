# usr/bin/python
# -*- coding:utf-8 -*-
# https://atcoder.jp/contests/abc323/tasks/abc323_c

import io
import sys

##########
_INPUT = """\
5 5
1000 1500 2000 2000 2500
xxxxx
oxxxx
xxxxx
oxxxo
oxxxx
"""
sys.stdin = io.StringIO(_INPUT)
##########

def abc323c(scorelist,statuslist):
    playerscorelist = []
    answer = ""
    answerlist = []
    scorelist_int = []
    for i in range(len(scorelist)):
        scorelist_int.append(int(scorelist[i]))
    scorelist_sort = sorted(scorelist_int)

#    print(scorelist)
#    print(statuslist)
#    print(scorelist_sort)

# get player's score list
    bonus = 0
    for status in statuslist:
        bonus = bonus + 1
        score = 0 
        for i in range(0,len(status)):
            if status[i] == "o":
               score = score + int(scorelist[i])
#        print(status, score+bonus)
        playerscorelist.append(score + bonus)

    maxplayerscore = max(playerscorelist)

    playerNoSolveProblist = []
    for i in range(0,len(playerscorelist)):

# if a player has maxscore, needs no score
        if maxplayerscore == playerscorelist[i]:
            answerlist.append(0)
            continue

# get list of unsolved Problem for each players
        status = statuslist[i]
        playerNoSolveProblist = []
        for j in range(0,len(status)):
            if status[j] == "x":
                playerNoSolveProblist.append(scorelist[j])

# convert to Integer
        playerNoSolveProblist_int = []
        for j in range(len(playerNoSolveProblist)):
            playerNoSolveProblist_int.append(int(playerNoSolveProblist[j]))
        playerNoSolveProblist_sort = sorted(playerNoSolveProblist_int)

# add scores in order of highest score
# if the needscore > target score, it will be breaked.
        targetscore = int(maxplayerscore - playerscorelist[i])
        needscore = 0
        neednum = 0
        for j in range(len(playerNoSolveProblist_sort)-1,-1,-1):
            needscore = needscore + int(playerNoSolveProblist_sort[j])
            neednum = neednum + 1
            if (needscore > targetscore):
                    answerlist.append(neednum)
#                    print(playerNoSolveProblist_sort)
#                    print(targetscore,neednum)
                    break

#    print(answerlist)
    for i in range(0,len(answerlist)):
        answer = answer + str(answerlist[i]) + "\n"

    answer = answer.rstrip('\r\n')

    return answer


if __name__ == '__main__':
    statuslist = []
    n = int(input().split(" ")[0])
    scorelist = input().split(" ")
    for i in range(0,n):
        statuslist.append(str(input()))
        
    print(abc323c(scorelist,statuslist))
