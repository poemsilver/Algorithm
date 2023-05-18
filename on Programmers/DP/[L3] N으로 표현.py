# https://school.programmers.co.kr/learn/courses/30/lessons/42895
from collections import defaultdict
def solution(N, number):
    if N == number:
        return 1
    
    graph = defaultdict(set)
    graph[1] = [N,-N]
    for i in range(2,7):
        vv2 = ''
        for j in range(i):
            vv2 += str(N)
        graph[i].add(int(vv2))
        graph[i].add(-int(vv2))
        for v in graph[i-1]:
            graph[i].add(v+N)
            graph[i].add(v-N)
            graph[i].add(v*N)
            graph[i].add(-v+N)
            graph[i].add(-v-N)
            graph[i].add(-v*N)
            if v > 0:
                graph[i].add(v//N)
                graph[i].add(N//v)
                graph[i].add(-v//N)
                graph[i].add(N//-v)
                
    for v in graph[2]:
        for i in range(3,7):
            if v != 0:
                for v2 in graph[i]:
                    graph[2+i].add(v+v2)
                    graph[2+i].add(v-v2)
                    graph[2+i].add(v*v2)
                    graph[2+i].add(-v+v2)
                    graph[2+i].add(-v-v2)
                    graph[2+i].add(-v*v2)
                    if v2 == 0:
                        continue
                    graph[2+i].add(v//v2)
                    graph[2+i].add(-v//v2)
    
    for v in graph[3]:
        for i in range(4,6):
            if v != 0:
                for v2 in graph[i]:
                    graph[3+i].add(v+v2)
                    graph[3+i].add(v-v2)
                    graph[3+i].add(v*v2)
                    graph[3+i].add(-v+v2)
                    graph[3+i].add(-v-v2)
                    graph[3+i].add(-v*v2)
                    if v2 == 0:
                        continue
                    graph[3+i].add(v//v2)
                    graph[3+i].add(-v//v2)
            
    for k in graph.keys():
        if number in graph[k]:
            return k
    return -1
