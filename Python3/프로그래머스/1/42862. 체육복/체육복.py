def solution(n, lost, reserve):
    students = [1 for _ in range(n)]
    
    for l in lost:
        students[l-1] = 0
    for r in reserve:
        students[r-1] += 1

    answer = 0  
    for idx, student in enumerate(students):
        if student == 0:
            if idx > 0 and students[idx-1] > 1:
                students[idx] = 1
                students[idx-1] = 1
            elif idx + 1 < n and students[idx+1] > 1:
                students[idx] = 1
                students[idx+1] = 1
            else:
                answer += 1   
    return n - answer