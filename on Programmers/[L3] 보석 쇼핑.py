# https://school.programmers.co.kr/learn/courses/30/lessons/67258

from collections import defaultdict
def solution(gems):
    answer = []
    
    #보석 종류 수
    kinds = len(set(gems))
    if kinds == 1:
        return [1,1]
    
    #시작,끝 포인터
    a,b = 0,0
    
    dic = defaultdict(int)
    dic[gems[0]] = 1
    
    leng = len(gems)
    
    #갱신해나갈 구간 길이
    path = leng
    answer = [0,leng-1]
    
    while a < leng and b < leng:
        #보석 종류 수 보다 현재 dic 보석 종류가 작을 때
        if len(dic.keys()) < kinds:
            b+=1
            if b == leng:
                break
            dic[gems[b]] += 1
        else:
            #현재 구간 길이가 더 작으면 갱신
            if (b-a+1) < path:
                answer = [a,b]
                path = b-a+1
            
            #만약 현재 a가 가르키는 보석의 종류가 1이면 그냥 삭제 아니면 하나 감소
            if dic[gems[a]] == 1:
                del dic[gems[a]]
            else:
                dic[gems[a]] -= 1
            a+=1
            
    return [answer[0]+1,answer[1]+1]
