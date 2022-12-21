# https://school.programmers.co.kr/learn/courses/30/lessons/43163

from collections import defaultdict, deque
def solution(begin, target, words):
    answer = 0
    # words에 존재하지 않으면 0
    if target not in words:
        return 0
    
    # key: 단어, value = 쌓인 변환 횟수
    visit = defaultdict(int)
    visit[begin] = 0
    q = deque([[begin,0]])
    
    while q:
        w,cnt = q.popleft()
        if w == target:
            answer = cnt
        
        # 다른 단어 갯수 check
        for i in range(len(words)):
            dif = 0
            for j in range(len(w)):
                if dif >= 2:
                    break
                if w[j] != words[i][j]:
                    dif += 1
            # 단어가 하나만 다르고 방문한 적 없는 단어면,
            if dif == 1 and visit[words[i]] == 0:
                visit[words[i]] = cnt+1
                q.append([words[i],cnt+1])
    
    return answer
