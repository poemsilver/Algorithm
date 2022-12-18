# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque
def solution(maps):
    answer = 0
    goal_x = len(maps)-1
    goal_y = len(maps[0])-1
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    q = deque()
    q.append([0,0])
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            newx = x+dx[i]
            newy = y+dy[i]
            
            #범위 내, 벽으로 막혀있지 않으면
            if 0<=newx<=goal_x and 0<=newy<=goal_y and maps[newx][newy] == 1:
                maps[newx][newy] = maps[x][y] + 1
                q.append([newx,newy])
    
    return maps[goal_x][goal_y] if maps[goal_x][goal_y] > 1 else -1
