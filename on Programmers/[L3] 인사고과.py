# https://school.programmers.co.kr/learn/courses/30/lessons/152995#

def solution(scores):
    answer = 1
    wanho = scores[0]
    wanho_s = sum(wanho)
    scores.sort(key = lambda x:(-x[0],x[1]))
    max_p = 0
    
    for a,b in scores:
        if wanho[0] < a and wanho[1] < b:
            return -1
        if max_p > b:
            continue
        max_p = max(max_p,b)
    
        if wanho_s < a+b:
            answer += 1
    
    return answer
