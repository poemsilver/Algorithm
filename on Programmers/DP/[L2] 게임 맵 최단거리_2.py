# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque
def solution(maps):
    answer = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q = deque()
    #(x,y)
    q.append((0,0))
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] +1
                q.append((nx,ny))
            
    return maps[-1][-1] if maps[-1][-1] > 1 else -1
