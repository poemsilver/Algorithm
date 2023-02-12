# https://school.programmers.co.kr/learn/courses/30/lessons/132266
# 다익스트라 알고리즘 적용

from collections import defaultdict,deque
def solution(n, roads, sources, destination):
    answer = [-1 for _ in range(len(sources))]
    M = 100001*n
    graph = defaultdict(list)
    # destination까지 최단거리 리스트
    dis = [M for _ in range(n+1)]
    for a,b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    q = deque()
    q.append((destination,0))
    while q:
        s,cost = q.popleft()
        
        for next in graph[s]:
            if next == destination:
                dis[next] = 0
            if cost+1 < dis[next]:
                dis[next] = cost+1
                q.append((next,cost+1))
                
    for i in range(len(sources)):
        s1 = sources[i]
        if dis[s1] == M:
            continue
        answer[i] = dis[s1]
    return answer
