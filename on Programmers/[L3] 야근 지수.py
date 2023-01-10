# https://school.programmers.co.kr/learn/courses/30/lessons/12927#

from heapq import heappush,heappop,heapify
def solution(n, works):
    answer = 0
    
    w = [-i for i in works]
    heapify(w)
    
    for _ in range(n):
        m = -(heappop(w))
        m -= 1
        if -m > 0:
            return 0
        heappush(w,-m)
    
    while w:
        answer += heappop(w)**2
    
    return answer
