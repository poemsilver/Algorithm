# https://school.programmers.co.kr/learn/courses/30/lessons/64062

def solution(stones, k):
    answer = 0
    
    # k칸을 뛰어넘지 않는 한도에서 최솟값을 이진탐색으로 구하자
    left = 1
    right = max(stones)
    
    while left <= right:
        mid = (right+left) // 2
        cnt = 0
        
        for i in range(len(stones)):
            if stones[i] - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        
        if cnt >= k:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
        
    return answer
