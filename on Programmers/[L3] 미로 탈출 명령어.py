# https://school.programmers.co.kr/learn/courses/30/lessons/150365
from collections import deque
def solution(n, m, x, y, r, c, k):
    # 거리와 k의 차이가 홀수면 답 x
    if abs(abs(x-r)+abs(y-c)-k)%2 == 1:
        return "impossible"
    q = deque()
    q.append((x,y,''))
    # d l r u
    dx = [1,0,0,-1]
    dy = [0,-1,1,0]
    while q:
        now_x,now_y,path = q.popleft()
        
        if (now_x,now_y) == (r,c) and (k-len(path))%2 == 1:
            break
        if (now_x,now_y) == (r,c) and len(path) == k:
            return path
        
        for i in range(4):
            xi = now_x+dx[i]
            yi = now_y+dy[i]
            if abs(xi-r)+abs(yi-c)+len(path)+1 > k: # 목적지 도달x인데 k 넘음
                continue
            if 0<xi<=n and 0<yi<=m:
                if i==0: # 아래
                    new_path = path+'d'
                elif i==1: # 왼
                    new_path = path+'l'
                elif i==2: # 오른
                    new_path = path+'r'
                else: # 위
                    new_path = path+'u'
                q.append((xi,yi,new_path))
                break # 최소 사전 경로만
    
    return "impossible"
