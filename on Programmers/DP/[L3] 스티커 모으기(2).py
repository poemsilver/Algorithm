# https://school.programmers.co.kr/learn/courses/30/lessons/12971#

def solution(sticker):
    n = len(sticker)
    if n == 1:
        return sticker[0]
    if n == 2:
        return max(sticker)
    if n == 3:
        return max(sticker[0]+sticker[2],sticker[1])
    
    #0,1번째 스티커를 처음으로 떼어낼 때 dp 배열
    dp = [[i for i in sticker] for _ in range(2)]
    dp[0][1] = 0
    dp[0][2] += dp[0][0]
    dp[1][0] = 0
    
    for j in range(3,n-1):
        dp[0][j] += max(dp[0][j-2],dp[0][j-3])
    
    for j in range(3,n):
        dp[1][j] = sticker[j] + max(dp[1][j-2],dp[1][j-3])
    
    return max(max(dp[0]),max(dp[1]))
