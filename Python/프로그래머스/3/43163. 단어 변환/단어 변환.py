from collections import deque

def one_word(cur, next_):
    cnt = 0
    for i, c in enumerate(cur):
        if c != next_[i]:
            cnt += 1
    return True if cnt == 1 else False

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    
    visited = {}
    for word in words:
        visited[word] = 0
    visited[begin] = 0
        
    queue = deque()
    queue.append(begin)
    while queue:
        cur = queue.popleft()
        if cur == target:
            answer = visited[cur]
            break
        
        for next_ in words:
            if not visited[next_] and one_word(cur, next_):
                queue.append(next_)
                visited[next_] = visited[cur] + 1
    return answer