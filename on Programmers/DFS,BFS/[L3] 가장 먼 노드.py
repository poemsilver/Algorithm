# https://school.programmers.co.kr/learn/courses/30/lessons/49189

#풀이 1
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


# 풀이2

from collections import defaultdict,deque
def solution(n, edge):
    answer = 0
    node = defaultdict(list)
    for i,j in edge:
        node[i].append(j)
        node[j].append(i)
        
    visit = [50001 for _ in range(n+1)]
    visit[0] = 0
    visit[1] = 0
    
    q = deque([[1,1]])
    
    while q:
        p,cnt = q.popleft()
        
        for i in node[p]:
            if cnt < visit[i]:
                visit[i] = cnt
                q.append([i,cnt+1])
                    
    visit.sort(reverse = True)
    M = visit[0]
    for i in visit:
        if i == M:
            answer += 1
        else:
            break
            
    return answer
