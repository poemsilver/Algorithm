# https://www.acmicpc.net/problem/13460

import sys
from collections import deque
# N줄 x M개씩
n, m = map(int, input().split())
gmap = []
b = []
r = []
hole = []
# map 생성, r b hole 좌표
for i in range(n):
    row = list(input().strip())
    for j in range(m):
        if row[j] == 'R':
            r = [i,j]
        elif row[j] == 'B':
            b = [i,j]
        elif row[j] == 'O':
            hole = [i,j]
    gmap.append(row)

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# dir 방향으로 갈 수 있는 곳까지 갈 수 있도록
def checklimit(xy, dir):
    x = xy[0]
    y = xy[1]
    dis = 0
    while 1:
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0<=nx<n and 0<=ny<m and gmap[nx][ny] != '#':
            dis += 1
            x = nx
            y = ny
            if gmap[nx][ny] == 'O':
                break
        else:
            break
    return [x,y],dis

visit = set()
visit.add((r[0],r[1],b[0],b[1]))
q = deque()
q.append((r,b,0))
answer = -1
while q:
    red,blue,cnt = q.popleft()
    # 구멍에 도달
    if red == hole:
        answer = cnt
        break

    # 10번 움직였는데 아직 hole에 도달 못함 => 해당 루트 stop
    if cnt >= 10:
        continue

    for i in range(4):
        rx = red[0] + dx[i]
        ry = red[1] + dy[i]
        bx = blue[0] + dx[i]
        by = blue[1] + dy[i]

        # 빨간공이 진행할 수 있는 방향이면
        if 0<=rx<n and 0<=ry<m and gmap[rx][ry] != '#' and (rx,ry) != (blue[0],blue[1]) and (rx,ry,bx,by) not in visit:
            new_red,r_dis = checklimit(red,i)
            new_blue,b_dis = checklimit(blue,i)
        elif 0<=bx<n and 0<=by<m and gmap[bx][by] != '#' and (bx,by) != (red[0],red[1]) and (rx,ry,bx,by) not in visit:
            new_red,r_dis = checklimit(red,i)
            new_blue,b_dis = checklimit(blue,i)
        else:
            continue

        # 파란공이 구멍에 빠졌으면 해당 루트 stop
        if new_blue == hole:
            continue

        # 빨간공과 파란공이 같은 곳에 있으면 이동거리 긴 공을 한 칸 후퇴
        if new_red == new_blue:
            if r_dis < b_dis:
                new_blue = [new_blue[0]-dx[i], new_blue[1]-dy[i]]
            else:
                new_red = [new_red[0]-dx[i], new_red[1]-dy[i]]

        if (new_red[0],new_red[1],new_blue[0],new_blue[1]) not in visit:
            visit.add((new_red[0],new_red[1],new_blue[0],new_blue[1]))
            q.append((new_red,new_blue,cnt+1))
print(answer)
