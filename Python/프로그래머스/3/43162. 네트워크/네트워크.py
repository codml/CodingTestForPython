def dfs(cur, n, computers, isNet, visited):
    visited[cur] = True
    isNet[cur] = True
    for i in range(n):
        if cur != i and computers[cur][i] == 1 and not visited[i]:
            dfs(i, n, computers, isNet, visited)

def solution(n, computers):
    netCnt = 0
    isNet = [False for _ in range(n)]
    
    for i in range(n):
        if isNet[i]:
            continue
        netCnt += 1
        visited = [False for _ in range(n)]
        dfs(i, n, computers, isNet, visited)
        
    answer = netCnt
    return answer
