# https://school.programmers.co.kr/learn/courses/30/lessons/84021

from collections import defaultdict, deque
def solution(game_board, table):
    answer = 0
    #game_boar용
    q1 = deque([(0,0)])
    #table용
    q2 = deque([(0,0)])
    #game_board의 빈공간 찾기
    #table의 빈공간 찾기
    MAX_X = len(game_board)
    MAX_Y = len(game_board[0])
    #방문용도
    visit_g = [[0 for _ in range(MAX_X)] for _ in range(MAX_Y)]
    visit_t = [[0 for _ in range(MAX_X)] for _ in range(MAX_Y)]

    def findzero(board, p, visit,target):
        for x in range(MAX_X):
            for y in range(MAX_Y):
                if visit[x][y] == 0 and board[x][y] == target:
                    visit[x][y] = 2
                    return (x,y)
                elif visit[x][y] == 0:
                    visit[x][y] = 1
        return 0

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    list_g = []
    list_t = []

    def findempty(board,q,empty,visit,target):
        t = []
        while q:
            x1, y1 = q.popleft()

            if board[x1][y1] != target:
                temp = findzero(board,(x1, y1),visit,target)
                if temp != 0:
                    q.append(temp)

            else:
                # 빈공간 첫 시작
                if t == []:
                    t.append((x1, y1))
                    visit[x1][y1] = 2
                cnt = 0
                for i in range(4):
                    nx = x1 + dx[i]
                    ny = y1 + dy[i]

                    if 0 <= nx < MAX_X and 0 <= ny < MAX_Y and visit[nx][ny] == 0 and board[nx][ny] == target:
                        visit[nx][ny] = 2
                        cnt += 1
                        t.append((nx, ny))
                        q.append((nx, ny))

                # 빈 공간의 끝이고 q1에 남아있는 것이 없음
                if cnt == 0 and not q:
                    xx = [t[i][0] for i in range(len(t))]
                    yy = [t[i][1] for i in range(len(t))]
                    p_x = max(xx) - min(xx)
                    p_y = max(yy) - min(yy)

                    p = [[0 for _ in range(p_y+1)] for _ in range(p_x+1)]
                    cx,cy = 0,0
                    for i in range(min(xx),max(xx)+1):
                        for j in range(min(yy),max(yy)+1):
                            if (i,j) in t:
                                p[cx][cy] = 1
                            cy += 1
                        cy = 0
                        cx += 1

                    empty.append(p)
                    t = []
                    temp = findzero(board, (x1, y1),visit,target)
                    if temp != 0:
                        q.append(temp)
        return empty


    list_g = findempty(game_board,q1,list_g,visit_g,0)
    list_t = findempty(table,q2,list_t,visit_t,1)

    def rotate_90(l2):
        x = len(l2)
        y = len(l2[0])
        result = [[0 for _ in range(x)] for _ in range(y)]

        for i in range(x):
            for j in range(y):
                result[j][x-1-i] = l2[i][j]

        return result

    def counter(l):
        xl = len(l)
        yl = len(l[0])
        cnt = 0

        for i in range(xl):
            for j in range(yl):
                if l[i][j] == 1:
                    cnt += 1

        return cnt

    for l in list_g:
        for i in range(len(list_t)):
            l2 = list_t[i]
            if l2 != 0 and ((len(l) == len(l2) and len(l[0]) == len(l2[0])) or (len(l) == len(l2[0]) and len(l[0]) == len(l2))):
                if l == l2:
                    answer += counter(l)
                    list_t[i] = 0
                    break
                elif l == rotate_90(l2):
                    answer += counter(l)
                    list_t[i] = 0
                    break
                elif l == rotate_90(rotate_90(l2)):
                    answer += counter(l)
                    list_t[i] = 0
                    break
                elif l == rotate_90(rotate_90(rotate_90(l2))):
                    answer += counter(l)
                    list_t[i] = 0
                    break
    return answer
