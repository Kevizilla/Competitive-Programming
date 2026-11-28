// Problem: Find Winner on a Tic Tac Toe Game
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
// Solved on: 2026-11-28T09:39:36.196Z

class Solution(object):
    def tictactoe(self, moves):
        n={}
        x=[]
        y=[]
        for i in range(len(moves)):
            if i%2==0:
                x.append(moves[i])
            else:
                y.append(moves[i])
        n['x']=x
        n['y']=y
        flag1=0
        flag2=0
        flag3=0
        for i in n['x']:
            for j in range(1,3):
                if[i[0]+j,i[1]] in n['x']:
                    flag1+=1
                if [i[0] , i[1]+j] in n['x']:
                    flag2 += 1
            if flag1==2 or flag2==2:
                break
            flag1=0
            flag2=0
        if flag1 == 2 or flag2 == 2:
            return "A"
        flag3+=1
        for i in n['y']:
            for j in range(1,3):
                if[i[0]+j,i[1]] in n['y']:
                    flag1+=1
                if [i[0] , i[1]+j] in n['y']:
                    flag2 += 1
            if flag1==2 or flag2==2:
                break
            flag1=0
            flag2=0
        if flag1 == 2 or flag2 == 2:
            return "B"
        flag3+=1
        for i in n['x']:
            if i[0]==i[1]:
                flag1+=1
        if flag1 == 3 or flag2 == 3:
            return "A"
        flag3+=1
        flag2=0
        flag1=0
        for i in n['y']:
            if i[0]==i[1]:
                flag1+=1
        if flag1 == 3 or flag2 == 3:
            return "B"
        flag3+=1

        if [1,1] in n['x'] and [0,2] in n['x'] and [2,0] in n['x']:
            return "A"
        elif [1,1] in n['y'] and [0,2] in n['y'] and [2,0] in n['y']:
            return "B"
        flag3+=1
        if flag3==5 and len(moves)==9:
            return "Draw"
        else:
            return "Pending"