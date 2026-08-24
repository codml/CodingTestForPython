

def solution(n):
    chess = [0 for _ in range(n)]
    
    def is_possible(cur, col, chess):
        for i in range(cur):
            if chess[i] == col or chess[i] - col == i - cur or chess[i] - col == cur - i:
                return False
        return True
    
    def backtrack(cur, chess):
        if cur == n:
            return 1
        
        answer = 0
        
        for i in range(n):
            if is_possible(cur, i, chess):
                chess[cur] = i
                answer += backtrack(cur + 1, chess)
                
        return answer
    return backtrack(0, chess)