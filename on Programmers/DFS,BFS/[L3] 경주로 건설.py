# https://school.programmers.co.kr/learn/courses/30/lessons/67259

from collections import deque
def solution(board):
    answer = 600*25
    M = 600*25
    n = len(board)
    dp = [[[M for _ in range(n)] for _ in range(n)] for _ in range(4)]
    
    # 방향 초기화
    for i in range(4):
        dp[i][0][0] = 0
    
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    q = deque()
    #(x,y,방향,비용)
    #시작할 때는 0과 1방향만 있으므로
    q.append((0,0,0,0))
    q.append((0,0,1,0))
    
    while q:
        x,y,d,c = q.popleft()
        
        if (x,y) == (n-1,n-1):
            continue
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
                
            if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0:
                # 진행방향이 달라질 때
                if i != d:
                    if c+6 < dp[i][nx][ny]:
                        dp[i][nx][ny] = c+6
                        q.append((nx,ny,i,c+6))
                else:
                    if c+1 <= dp[i][nx][ny]:
                        dp[i][nx][ny] = c+1
                        q.append((nx,ny,i,c+1))
    for i in range(4):
        answer = min(answer,dp[i][-1][-1])
    return answer*100
