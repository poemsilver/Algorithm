# https://school.programmers.co.kr/learn/courses/30/lessons/12904#

def solution(s): 
    l = len(s)
    
    if len(s) == 1:
        return 1
    
    while l != 1:
        cnt = 1
        for j in range(len(s)-l+1):
            cnt = 1
            for i in range(l//2):
                if s[j+i] == s[l+j-i-1]:
                    cnt+=2
                else:
                    break
            if cnt >= l:
                break
        
        if cnt >= l:
            break
        else:
            l -= 1

    return l
