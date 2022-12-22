# https://school.programmers.co.kr/learn/courses/30/lessons/87694

from collections import defaultdict,deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    # 102 x 102 만들기
    board = [[2] * 102 for _ in range(102)]

    # 테두리 그리기
    for r in rectangle:
        x1 = r[0] * 2
        x2 = r[2] * 2
        y1 = r[1] * 2
        y2 = r[3] * 2
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    board[i][j] = 0
                elif board[i][j] != 0:
                    board[i][j] = 1

    visit = defaultdict(int)
    visit[(characterX*2,characterY*2)] = 1
    q = deque([(characterX*2,characterY*2,1)])
    
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    while q:
        x,y,cnt = q.popleft()
        
        if x == itemX*2 and y == itemY*2:
            answer = (cnt-1)//2
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if board[nx][ny] == 1 and visit[(nx,ny)] != 1:
                q.append((nx,ny,cnt+1))
                visit[(nx,ny)] = 1

    return answer
