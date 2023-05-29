# dp 풀이
# https://school.programmers.co.kr/learn/courses/30/lessons/118668
def solution(alp, cop, problems):
    alp_p = sorted(problems, key=lambda x: x[0])
    cop_p = sorted(problems, key=lambda x: x[1])
    goal_alp = alp_p[-1][0]
    goal_cop = cop_p[-1][1]
    dp = [[101 * (goal_alp+goal_cop) for _ in range(goal_cop + 1)] for _ in range(goal_alp + 1)]

    alp = min(alp, goal_alp)
    cop = min(cop, goal_cop)
    dp[alp][cop] = 0

    # 학습 vs 문제풀기
    for now_alp in range(alp,goal_alp+1):
        for now_cop in range(cop,goal_cop+1):
            # 학습
            if now_alp + 1 <= goal_alp:
                dp[now_alp+1][now_cop] = min(dp[now_alp+1][now_cop],dp[now_alp][now_cop]+1)
            if now_cop + 1 <= goal_cop:
                dp[now_alp][now_cop+1] = min(dp[now_alp][now_cop+1],dp[now_alp][now_cop]+1)
        
            # 문제풀기
            for areq,creq,i,j,c in problems:
                if now_alp >= areq and now_cop >= creq: # 문제 요구사항 충족
                    new_alp = min(goal_alp,now_alp+i)
                    new_cop = min(goal_cop,now_cop+j)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop],dp[now_alp][now_cop]+c)
    
    return dp[goal_alp][goal_cop]
