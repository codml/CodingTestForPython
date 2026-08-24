from heapq import heappush, heappop, heapify

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    while scoville and scoville[0] < K: 
        if len(scoville) < 2:
            answer = -1
            break
        f = heappop(scoville)
        s = heappop(scoville)
        heappush(scoville, f+s*2)
        answer += 1
        
    return answer