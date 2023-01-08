# https://school.programmers.co.kr/learn/courses/30/lessons/42861#

# Kruskal 알고리즘

def solution(n, costs):
    answer = 0
    
    # cost기준으로 낮은 것부터 정렬
    costs.sort(key = lambda x:x[2])
    
    # 연결 확인 용도
    graph = set([costs[0][0]])
    
    while len(graph) < n:
        for i,j,c in costs:
            if i in graph and j in graph:
                continue
            # 둘 중 하나만 graph에 있으면(연결 안되어있으면)
            if i in graph or j in graph:
                # 여러 개의 값을 넣을 때는 update, 하나는 add
                graph.update([i,j])
                answer += c
                break
                
    return answer
