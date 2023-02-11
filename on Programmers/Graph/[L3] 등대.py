# https://school.programmers.co.kr/learn/courses/30/lessons/133500#

from collections import defaultdict,deque
def solution(n, lighthouse):
    graph = defaultdict(list)
    onoff = [0 for _ in range(n + 1)]

    for a, b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)

    q = deque()
    # 리프 노드 담기
    for i in range(1, n+1):
        if len(graph[i]) == 1:
            q.append(i)

    # 리프 노드부터 루트까지 올라가기, 등대 켜지면 다음 노드와 연결 끊기
    while q:
        now_leaf = q.popleft()
        if graph[now_leaf] == []:
            break
        parent = graph[now_leaf][0]

        # 리프 노드 그래프에서 삭제
        del graph[now_leaf]
        # 부모 노드에서 리프 노드 연결 해제
        graph[parent].remove(now_leaf)
        # 부모 노드가 리프 노드가 되면 큐에 넣기
        if len(graph[parent]) == 1:
            q.append(parent)

        if onoff[now_leaf] == 1:
            continue
        onoff[parent] = 1
    
    return sum(onoff)
