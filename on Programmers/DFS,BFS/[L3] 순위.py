# https://school.programmers.co.kr/learn/courses/30/lessons/49191#

from collections import deque
def solution(n, results):
    answer = 0
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
    visit = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i,j in results:
        graph[i][i] = 1
        graph[j][j] = 1
        graph[i][j] = 1
        graph[j][i] = -1

    def bfs(p):
        visit[p][p] = 1
        q = deque()

        for i in range(len(graph[p])):
            if i != p and graph[p][i] != 0:
                q.append(i)

        while q:
            now = q.popleft()
            # 승점 포인트를 가지게 해준 대상 선수(=이긴 선수)가 이겨버린 선수는 내가 이길 수 있는 선수이므로 방문 하지 않았다면 방문 후 큐에 넣기
            if graph[p][now] == 1:
                for i in range(len(graph[now])):
                    if graph[now][i] == 1 and visit[p][i] == 0:
                        graph[p][i] = 1
                        visit[p][i] = 1
                        q.append(i)

            # 패점 포인트를 가지게 해준 대상 선수(=진 선수)가 져버린 선수는 내가 져버리는 선수이므로 방문 하지 않았다면 방문 후 큐에 넣기
            if graph[p][now] == -1:
                for i in range(len(graph[now])):
                    if graph[now][i] == -1 and visit[p][i] == 0:
                        graph[p][i] = -1
                        visit[p][i] = 1
                        q.append(i)

    for p in range(1,n+1):
        bfs(p)
    
    for p in range(1,n+1):
        cnt = 0
        for i in range(1,n+1):
            if graph[p][i] != 0:
                cnt += 1
        if cnt == n:
            answer += 1
    
    return answer
