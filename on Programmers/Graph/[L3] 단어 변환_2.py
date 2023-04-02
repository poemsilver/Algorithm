# https://school.programmers.co.kr/learn/courses/30/lessons/43163

from collections import defaultdict,deque
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    
    visit = defaultdict(int)
    q = deque()
    q.append((begin,0))
    visit[begin] = 1
    while q:
        w,cost = q.popleft()
        if w == target:
            answer = cost
            break
        
        for i in range(len(words)):
            dif = 0
            if words[i] != w and words[i] not in visit.keys():
                for k in range(len(words[i])):
                    if words[i][k] != w[k]:
                        dif += 1
                    if dif > 1:
                        break
            if dif == 1:
                visit[words[i]] = 1
                q.append((words[i],cost+1))
        
    return answer
