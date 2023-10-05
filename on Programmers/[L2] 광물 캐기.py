# https://school.programmers.co.kr/learn/courses/30/lessons/172927#
from copy import deepcopy
from collections import defaultdict
def solution(picks, minerals):
    answer = 0
    can_use = deepcopy(picks)
    list_f = defaultdict(list)
    list_f["diamond"] = [1,5,25]
    list_f["iron"] = [1,1,5]
    list_f["stone"] = [1,1,1]
    list_f["n/a"] = [0,0,0]
    
    # 피로도 내림차순
    # 5개씩 묶기, 순서대로 처리해야하므로 곡괭이 수에 맞춰 자르기
    s_minerals = []
    if sum(picks)*5 >= len(minerals):
        s_minerals = minerals
    else:
        s_minerals = minerals[:sum(picks)*5]
    cost = defaultdict(int)
    for i in range(len(s_minerals)):
        cost[i//5] += list_f[s_minerals[i]][2]
    
    # value 내림차순으로 정렬, 딕셔너리로 변환
    sorted_cost = dict(sorted(cost.items(), key=lambda item: item[1], reverse=True))
    sorted_minerals = []
    for k in sorted_cost.keys():
        if k*5+5 > len(s_minerals):
            sorted_minerals+=s_minerals[k*5:]
            sorted_minerals+=['n/a']*((k*5+5)-len(s_minerals))
        else:
            sorted_minerals+=s_minerals[k*5:k*5+5]
    # picks 한 번씩 돌기. 피로도 합보다 크면 break
    # 한 번 다 돌면 answer에 더하고
    # 최소값을 가진 곡괭이 하나 차감.
    # 잔여 곡괭이가 0이면 종료
    start_p = 0
    end_p = 0
    # 초기 minerals index 세팅
    if len(minerals) >= 5:
        end_p = 4
    else:
        end_p = len(minerals)-1
    
    # 탐색 시작
    while sum(can_use) != 0:
        min_sum = 25*(len(minerals)+25)
        min_pick = 0
        for i in range(len(picks)):
            if can_use[i] == 0:
                continue
            temp = 0
            for p in range(start_p,end_p+1):
                temp += list_f[sorted_minerals[p]][i]
                if temp > min_sum:
                    break
            if temp < min_sum:
                min_sum = temp
                min_pick = i
        answer += min_sum
        can_use[min_pick] -= 1
        if start_p+5 >= len(sorted_minerals):
            break
        elif end_p+5 >= len(sorted_minerals):
            end_p = len(sorted_minerals)-1
            start_p += 5
        else:
            end_p += 5
            start_p += 5
        
    return answer
