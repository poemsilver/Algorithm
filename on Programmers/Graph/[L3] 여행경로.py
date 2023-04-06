#https://school.programmers.co.kr/learn/courses/30/lessons/43164

from collections import defaultdict
def solution(tickets):
    answer = []
    t_list = defaultdict(list)
    # t_list
    for i in range(len(tickets)):
        s = tickets[i][0]
        t = tickets[i][1]
        t_list[s].append((t,i))
        t_list[s].sort()
        
    visit = set([])
    def dfs(start,t_list,path,visit):
        nonlocal answer
        if answer != []:
            return answer
        # 해당 start의 value 없음
        if len(path) == len(tickets)+1:
            # 경로 모두 포함했으면 answer에 넣기
            answer = path
            return answer
        
        for arr_num in t_list[start]:
            arr = arr_num[0]
            n = arr_num[1]
            if (start,arr,n) not in visit:
                visit.add((start,arr,n))
                dfs(arr,t_list,path+[arr],visit)
                visit.remove((start,arr,n))
    
    dfs('ICN',t_list,['ICN'],visit)
    return answer
