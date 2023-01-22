# https://school.programmers.co.kr/learn/courses/30/lessons/12907#

def solution(n, money):
    money.sort()
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    
    for m in money:
        for cur in range(1,n+1):
            if m > cur:
                continue
            dp[cur] += dp[cur-m]
            
    return dp[-1]%1000000007
