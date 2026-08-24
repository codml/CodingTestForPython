from collections import defaultdict

def solution(tickets):
    routes = defaultdict(list)
    
    for ticket in tickets:
        arr = ticket[0]
        dep = ticket[1]
        routes[arr].append(dep)
        routes[arr].sort()
    
    def dfs(cur, answer):
        if len(answer) - 1 == len(tickets):
            return answer

        for idx, next_ in enumerate(routes[cur]):
            routes[cur].pop(idx)
            result = dfs(next_, answer + [next_])
            routes[cur].insert(idx, next_)
            if result:
                return result
        return None
    
    answer = dfs('ICN', ['ICN'])
    return answer