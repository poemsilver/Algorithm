from queue import PriorityQueue
def solution(jobs):
    answer = 0
    q = PriorityQueue()
    
    for s,f in jobs:
        q.put((s+f,(s,f)))
    for _ in range(len(jobs)):
        p,job = q.get()
        answer += answer + job[1] - job[0]
        
    return answer//len(jobs)
