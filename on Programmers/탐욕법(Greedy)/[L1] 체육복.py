# https://school.programmers.co.kr/learn/courses/30/lessons/42862?language=python3

def solution(n, lost, reserve):

    # 여분도 없는데 잃어버림
    lost_p = set(lost) - set(reserve)
    # 여분 있는데 안잃어버림
    rese_p = set(reserve) - set(lost)
    
    for i in rese_p:
        if i-1 in lost_p:
            lost_p.remove(i-1)
        elif i+1 in lost_p:
            lost_p.remove(i+1)
            
    return n-len(lost_p)
