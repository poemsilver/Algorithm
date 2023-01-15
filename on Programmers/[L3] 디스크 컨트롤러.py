# https://school.programmers.co.kr/learn/courses/30/lessons/42627

from queue import PriorityQueue
def solution(jobs):
    answer = 0
    q = PriorityQueue()
    n = len(jobs)
    # 현재 시점
    cur_t = 0
    # 현재 쌓인 작업소요시간
    cur_c = 0
    
    while 1:
        temp = []
        # 현재 시점보다 작업 요청시간이 작거나 같으면
        for t,c in jobs:
            if t <= cur_t:
                # 작업소요시간(cost)가 작은 순대로 우선순위큐
                q.put((c,t))
            else:
                temp.append([t,c])
        # jobs 갱신(현재 q에 들어가지 않은 것들로)
        jobs = temp
        
        # 더 이상 작업할 것 없음
        if q.empty() == True and jobs == []:
            break
        
        # 작업물은 남았지만 현재 시점에서 작업할 수 있는 work 없음
        if q.empty() == True:
            cur_t += 1
        else:
            work_c, work_t = q.get()
            cur_t += work_c
            cur_c += cur_t - work_t
        
    return cur_c//n
