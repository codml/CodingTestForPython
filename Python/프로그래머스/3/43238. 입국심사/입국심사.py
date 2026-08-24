def cal_people(arr, time, target):
    people = 0
    flag = False
    for a in arr:
        people += time // a
        if not flag and time % a == 0:
            flag = True
    return people, flag

def binary_search(arr, target, f, r):
    while f <= r:
        mid = (f + r) // 2
        people, flag = cal_people(arr, mid, target)
        if people == target and flag:
            return mid
        elif (people == target and not flag) or people > target:
            r = mid - 1
        else:
            f = mid + 1
    return f
    
def solution(n, times):
    min_ = min(times)
    answer = binary_search(times, n, 0, min_*n)
    return answer