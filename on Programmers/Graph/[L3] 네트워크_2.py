# https://school.programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    answer = 0
    visit = [0 for _ in range(n)]
    
    def dfs(x):
        visit[x] = 1
        # 깊이 탐색해서 연결된 노드 방문 표시
        for j in range(n):
            if x != j and computers[x][j] == 1 and visit[j] == 0:
                dfs(j)
            
    for i in range(n):
        if visit[i] == 0:
            dfs(i)
            answer += 1
        
    return answer
