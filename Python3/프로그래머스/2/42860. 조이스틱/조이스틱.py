def a_next(name, i):
    for cur in range(i+1, len(name)):
        if name[cur] != 'A':
            return cur
    return len(name)

def solution(name):
    answer = 0
    min_move = len(name) - 1
    
    for i in range(len(name)):
        answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        next_ = a_next(name, i)
        min_move = min(min_move, i*2 + len(name)-next_, (len(name)-next_)*2+i)
        
    answer += min_move
    return answer