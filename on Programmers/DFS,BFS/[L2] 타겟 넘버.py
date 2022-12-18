#https://school.programmers.co.kr/learn/courses/30/lessons/43165

def dfs(numbers,cnt,sum,target):
    global answer
    if cnt == len(numbers)-1:
        if sum+numbers[cnt] == target:
            answer+=1
        if sum-numbers[cnt] == target:
            answer+=1
            
        return answer

    dfs(numbers,cnt+1,sum+numbers[cnt],target)
    dfs(numbers,cnt+1,sum-numbers[cnt],target)
        
def solution(numbers, target):
    global answer
    answer = 0
    sum = 0
    cnt = 0

    dfs(numbers,cnt,sum,target)

    return answer
