# https://www.acmicpc.net/problem/3190

import sys
from collections import deque
n = int(input()) # 맵 길이 n*n
board = [[0 for _ in range(n+1)] for _ in range(n+1)]
board[1][1] = 1 # 초기 뱀 위치
k = int(input()) # 사과 갯수
for _ in range(k): # 사과 위치 -> 2
    x,y = input().split()
    board[int(x)][int(y)] = 2

l = int(input()) # 뱀 방향 변환 정보 갯수
info = deque()
for _ in range(l):
    tmp = list(map(str,sys.stdin.readline().split()))
    info.append([int(tmp[0]),tmp[1]])

t = 0
# D : 오른쪽, L : 왼쪽, 초기 방향 D
q = deque()
# 현재 뱀 머리 위치, 뱀의 현재 방향, 첫 뱀의 방향 변환 정보
# 뱀의 현재 방향 : [상,하,좌,우] = [0,1,2,3]
first_info = info.popleft()
q.append(([1,1], 3, first_info, deque([[1,1]])))
while q:
    p, now, change, tail = q.popleft()
    dir = 0
    if t >= change[0] and change != [0,0]: # 변환 시간이면
        dir = change[1]
        if info:
            change = info.popleft()
        else:
            change = [0,0]

    # 뱀 머리 위치에 따른 진행 방향 설정
    if now == 3: # 현재 오른쪽(+y방향)
        if dir == 0 :
            p[1] += 1
        elif dir == 'D':
            p[0] += 1
            now = 1
        else:
            p[0] -= 1
            now = 0
    elif now == 2: # 왼쪽(-y방향)
        if dir == 0 :
            p[1] -=1
        elif dir == 'D':
            p[0] -= 1
            now = 0
        else:
            p[0] += 1
            now = 1
    elif now == 1: # 하(+x방향)
        if dir == 0 :
            p[0] +=1
        elif dir == 'D':
            p[1] -= 1
            now = 2
        else:
            p[1] += 1
            now = 3
    else: # 상(-x방향)
        if dir == 0 :
            p[0] -=1
        elif dir == 'D':
            p[1] += 1
            now = 3
        else:
            p[1] -= 1
            now = 2

    if p[0] <= 0 or p[0] > n or p[1] <= 0 or p[1] > n: # board 범위 벗어나거나
        break
    if board[p[0]][p[1]] == 1: # 자신의 몸통에 닿으면
        break

    t += 1
    if board[p[0]][p[1]] == 0: # 사과 없음
        del_p = tail.popleft()
        board[del_p[0]][del_p[1]] = 0 # 꼬리부분 0처리
    tail.append([p[0],p[1]]) # tail.append(p) 넣으면 이후 변경된 p값으로 계속 변함.
    board[p[0]][p[1]] = 1
    q.append((p, now, change,tail))
print(t+1)
