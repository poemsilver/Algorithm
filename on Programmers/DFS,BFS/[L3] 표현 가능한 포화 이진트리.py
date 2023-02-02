# https://school.programmers.co.kr/learn/courses/30/lessons/150367

def solution(numbers):
    answer = [1 for _ in range(len(numbers))]
    n = []
    
    for num in numbers:
        v = format(num,"b")
        nn = len(v)
        init = 1
        i = 1
        while init < nn:
            i += 1
            init = 2**i -1
        n.append('0'+'0'*(init-nn)+v)

    def dfs(node,start,end):
        nonlocal result
        root = (start+end)//2
        if root%2 == 1:
            return
        left = start + (root-start)//2
        right = end - (end-root)//2
        if node[root] == '0' and (node[left] == '1' or node[right] == '1'):
            result = 0
            return
        dfs(node,root+1,end)
        dfs(node,start,root-1)
        
    # 루트 트리가 0인데 서브가 1 경우를 찾기(dfs)
    for i in range(len(n)):
        node = n[i]
        nn = len(node)-1
        result = 1
        dfs(node,1,nn)
        if result == 0:
            answer[i] = 0
        
    return answer
