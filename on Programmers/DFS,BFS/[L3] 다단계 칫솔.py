# https://school.programmers.co.kr/learn/courses/30/lessons/77486

from collections import deque
def solution(enroll, referral, seller, amount):
    answer = [0 for _ in range(len(enroll))]
    # 그래프 만들기
    graph = {}
    i = 0
    for e,r in zip(enroll, referral):
        graph[e] = [r, i]
        i += 1

    # (seller, 수익금) 해당 seller부터 상위 노드로 올라가며 수익 배분
    def bfs(s, profit):
        q = deque()
        q.append((s,profit))
        while q:
            cur_s, p = q.popleft()
            if cur_s == "-":
                break
            refe_s = graph[cur_s][0]
            next_p = p//10
            answer[graph[cur_s][1]] += p
            if next_p < 1:
                break
            answer[graph[cur_s][1]] -= next_p
            q.append((refe_s,next_p))
    
    # for문으로 (seller, 수익금) 돌리면서 result 갱신
    for i in range(len(seller)):
        bfs(seller[i],amount[i]*100)
    
    return answer
