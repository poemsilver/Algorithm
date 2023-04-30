# https://www.acmicpc.net/problem/12100
import sys
from copy import deepcopy

n = int(input())
board = []
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    board.append(temp)

# 최대 움직임 횟수가 5회이므로 모든 경로 탐색
# 첫 시작 경우의 수는 상,하,좌,우 4가지
# [상,하,좌,우] = [0,1,2,3]

# (현재 경우의 수에서 board, 진행 방향)
def move(path,dir):
    # 상
    if dir == 0:
        for y in range(n):
            # 가장 높은 우선순위
            p = 0
            # 상 -> 하 탐색
            for x in range(1,n):
                if path[x][y] == 0:
                    continue
                now = path[p][y]
                next = path[x][y]
                path[x][y] = 0
                if now == 0:
                    path[p][y] = next
                elif now == next:
                    path[p][y] += next
                    p += 1
                # now가 0도 아니고 next와 같지도 않을 때, 미리 다음 now의 값을 갱신
                else:
                    p += 1
                    path[p][y] = next
    # 하
    elif dir == 1:
        for y in range(n):
            p = n-1
            # 하 -> 상 탐색
            for x in range(n-2,-1,-1):
                if path[x][y] == 0:
                    continue
                now = path[p][y]
                next = path[x][y]
                path[x][y] = 0
                if now == next:
                    path[p][y] += next
                    p -= 1
                elif now == 0:
                    path[p][y] = next
                else:
                    p -= 1
                    path[p][y] = next
    # 좌
    elif dir == 2:
        for x in range(n):
            p = 0
            # 우 -> 좌 탐색
            for y in range(1,n):
                # 0이면 건너뜀
                if path[x][y] == 0:
                    continue
                now = path[x][p]
                next = path[x][y]
                path[x][y] = 0
                if now == next:
                    path[x][p] += next
                    path[x][y] = 0
                    p += 1
                elif now == 0:
                    path[x][p] = next
                    path[x][y] = 0
                else:
                    p += 1
                    path[x][p] = next
    # 우
    else:
        for x in range(n):
            p = n-1
            # 좌 -> 우 탐색
            for y in range(n-2,-1,-1):
                # 0이면 건너뜀
                if path[x][y] == 0:
                    continue
                now = path[x][p]
                next = path[x][y]
                path[x][y] = 0
                if now == next:
                    path[x][p] += next
                    p -= 1
                elif now == 0:
                    path[x][p] = next
                else:
                    p -= 1
                    path[x][p] = next
    return path

def dfs(board2,cnt,answer):
    if cnt >= 5:
        maxv = 0
        for i in range(n):
            maxv = max(maxv,max(board2[i]))
        answer.append(maxv)
        return

    for i in range(4):
        # 깊은 복사
        next_board = move(deepcopy(board2),i)
        dfs(next_board,cnt+1,answer)
    return answer

answer = dfs(board,0,[])
print(max(answer))
