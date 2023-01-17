# https://school.programmers.co.kr/learn/courses/30/lessons/68646

def solution(a):
    answer = [0 for _ in range(len(a))]
    
    left = 1000000001
    right = 1000000001
    
    for i in range(len(a)):
        #계속 왼,우측의 최솟값을 갱신해나감
        if a[i] < left:
            left = a[i]
            answer[i] = 1
        if a[len(a)-1-i] < right:
            right = a[len(a)-1-i]
            answer[len(a)-1-i] = 1
    
    return sum(answer)
