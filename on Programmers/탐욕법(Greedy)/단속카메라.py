# https://school.programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    r = len(routes)
    visit = [0 for _ in range(r)]
    camera = 0

    for i in range(r):
        if visit[i] == 0:
            camera = routes[i][1]
            answer += 1
        for j in range(i+1,r):
            if routes[j][0] <= camera <= routes[j][1] and visit[j]==0:
                visit[j] = 1

    return answer
