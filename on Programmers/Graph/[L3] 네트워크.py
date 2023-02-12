def solution(n, computers):
    answer = 0
    visit = [0]*n

    def dfs(x,visit):
        visit[x] = 1
        for j in range(n):
            if j != x and computers[x][j] == 1 and visit[j] == 0:
                dfs(j,visit)
        
    for i in range(n):
        if visit[i] == 0:
            dfs(i,visit)
            answer+=1

    return answer
