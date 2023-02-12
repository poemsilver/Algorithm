# 플루이드-와셜 알고리즘 적용 풀이

def solution(n, s, a, b, fares):
    answer = 100001 * n
    M = 100001 * n
    graph = [[M for _ in range(n+1)] for _ in range(n+1)]
    # 플로이드-워셜, 초기상태 정의
    for i,j,c in fares:
        graph[i][j] = c
        graph[j][i] = c
    
    # 자기 자신은 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                graph[i][j] = 0
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if graph[i][j] > graph[i][k]+graph[k][j]:
                    graph[i][j] = graph[i][k]+graph[k][j]

    for i in range(1,n+1):
        answer = min(answer,graph[i][s]+graph[i][a]+graph[i][b])
    
    return answer
