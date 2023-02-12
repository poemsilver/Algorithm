# https://school.programmers.co.kr/learn/courses/30/lessons/42898 

# DP로도 풀 수 있지만 BFS로도 풀 수 있음
from collections import deque
def solution(m, n, puddles):
    answer = 0
    visit = [[0 for _ in range(m)] for _ in range(n)]
    
    dx = [1,0]
    dy = [0,1]
    
    q = deque([(0,0)])
    visit[0][0] = 1
    
    while q:
        x,y = q.popleft()
        
        for i in range(2):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if [ny+1,nx+1] not in puddles:
                    visit[nx][ny] += visit[x][y]
                    if (nx,ny) not in q:
                        q.append((nx,ny))
    
    answer = visit[n-1][m-1]%1000000007
    return answer
