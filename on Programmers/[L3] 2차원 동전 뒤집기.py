# https://school.programmers.co.kr/learn/courses/30/lessons/131703#
# 테스트케이스 2번만 통과 못함..

from collections import deque
def solution(beginning, target):
    answer = 0
    if beginning == target:
        return 0
    x = len(beginning)
    y = len(beginning[0])
    
    # 뒤집기
    def flip(index,xy):
        # 행(x축) 뒤집기
        if xy == 1:
            trans = beginning[index]
            for i in range(y):
                trans[i] = 1 - trans[i]
            beginning[index] = trans
        # 열(y축) 뒤집기 (xy = 0)
        else:
            for xx in range(x):
                beginning[xx][index] = 1 - beginning[xx][index]
        return beginning
    
    # check = []
    # # 아예 정반대이면 행, 열 중 작은거 리턴
    # for xx in range(x):
    #     temp = [0 for _ in range(y)]
    #     for yy in range(y):
    #         temp[yy] = 1 - beginning[xx][yy]
    #     check.append(temp)
    # if check == target:
    #     return min(x,y)
    
    for x1 in range(x):
        now = beginning[x1]
        t = target[x1]
        if now == t:
            continue
        diff = 0
        for y1 in range(y):
            if now[y1] != t[y1]:
                diff += 1
        # 다른게 더 많으면 아예 반대로
        if diff > y/2:
            for y2 in range(y):
                if now[y2] == t[y2]:
                    # 해당 열 뒤집기
                    flip(y2,0)
                    answer += 1
            # 해당 행 뒤집기
            flip(x1,1)
            answer += 1
        # 타겟과 같게
        else:
            for y2 in range(y):
                if now[y2] != t[y2]:
                    flip(y2,0)
                    answer += 1
                    
    if beginning != target:
        return -1
    return answer
