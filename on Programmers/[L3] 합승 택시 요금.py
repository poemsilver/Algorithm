# 미완
# https://school.programmers.co.kr/learn/courses/30/lessons/72413?language=python3

from collections import defaultdict, deque
def solution(n, s, a, b, fares):
    answer = 0
    
    fares.sort(key = lambda x:x[2])
    graph = defaultdict(list)
    
    for i,j,c in fares:
        graph[i].append((j,c))
        graph[j].append((i,c))

    costs = [100001*n for _ in range(n+1)]
    costs[0] = 0
    costs[s] = 0
    
    q = deque()
    q.append([s,0])
    # S부터 각 지점까지 최단거리 구하기
    while q:
        now, c = q.popleft()
        for i,co in graph[now]:
            if costs[i] > c+co:
                costs[i] = c+co
                q.append([i,c+co])
    print(costs)
    
    # A지점부터 B지점까지 최단거리, 합승지점 구하기
    atob = [100001*n for _ in range(n+1)]
    atob[0] = 0
    atob[s] = 0
    q = deque()
    q.append([a,0,[a]])
    node = []
    while q:
        now,c,path = q.popleft()
        
        if now == b:
            node = path
            break
        
        for i,co in graph[now]:
            if atob[i] > c+co:
                atob[i] = c+co
                path.append(i)
                q.append([i,c+co,path])
    print(atob)
    print(node)
    return answer
