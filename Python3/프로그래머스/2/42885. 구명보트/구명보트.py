from collections import deque

def solution(people, limit):
    answer = 0
    deq = deque()
    
    people.sort()
    for person in people:
        deq.append(person)
    
    while deq:
        low = deq[0]
        high = deq[-1]
        if low + high <= limit:
            deq.popleft()
        if deq:
            deq.pop()
        answer += 1
    return answer