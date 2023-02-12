# https://school.programmers.co.kr/learn/courses/30/lessons/72413?language=python3

from collections import defaultdict,deque
def solution(n, s, a, b, fares):
    answer = n * 100001
    M = n * 100001
    # 최단거리 배열 return 다익스트라
    # graph[시작] = [끝,거리]
    def dij(start,graph):
        dis = [M for _ in range(n+1)]
        dis[start] = 0
        q = deque()
        q.append((start,0))
        
        while q:
            now,cost = q.popleft()
            
            for next,c in graph[now]:
                if c+cost < dis[next]:
                    dis[next] = c+cost
                    q.append((next,c+cost))
        
        return dis
    
    graph = defaultdict(list)
    for i,j,c in fares:
        graph[i].append([j,c])
        graph[j].append([i,c])
    
    dis1 = dij(s,graph)
    
    # 완전탐색 : 최단거리를 가지는 i 지점 찾기
    for i in range(n+1):
        # i지점부터 모든 지점까지 최단경로 저장
        dis2 = dij(i,graph)
        if dis1[i]+dis2[a]+dis2[b] < answer:
            answer = dis1[i]+dis2[a]+dis2[b]
        
    return answer
