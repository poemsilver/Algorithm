# https://school.programmers.co.kr/learn/courses/30/lessons/49189
from collections import defaultdict,deque

def solution(n, edge):
    answer = 0
    graph = defaultdict(list)
    INF = 50001
    visit = [INF for _ in range(n+1)]
    visit[0] = 0
    visit[1] = 0
    edge.sort()
    
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    #node,cnt 배열
    q = deque()
    
    for i in graph[1]:
        q.append([i,1])
    
    while q:
        node, cnt = q.popleft()
        
        #현재 경로가 최단경로 일 때
        if cnt < visit[node]:
            visit[node] = min(visit[node],cnt)
            
            cnt += 1
            for i in graph[node]:
                #출발점인 1이 아니면
                if visit[i] != 0:
                    q.append([i,cnt])
    visit.sort(reverse = True)
    MAX = max(visit)
    for i in visit:
        if i == MAX:
            answer+=1
        else:
            break
    return answer
