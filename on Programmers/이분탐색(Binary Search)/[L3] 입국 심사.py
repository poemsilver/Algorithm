# https://school.programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    answer = 0
    times.sort()
    
    left = 1
    right = max(times)*n
    
    while left <= right:
        mid = (left+right) // 2
        n2 = 0
        
        for t in times:
            n2 += mid // t
            if n2 >= n:
                break
        
        if n2 >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer
