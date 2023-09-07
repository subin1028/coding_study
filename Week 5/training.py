import copy
def solution(n, lost, reserve):
    answer = 0
    have = n - len(lost)
    lost.sort()
    reserve.sort()
    
    
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            continue
        
        if i+1 in reserve:
            have += 1
            reserve.remove(i+1)
            continue
        
        elif i-1 in reserve:
            have += 1
            reserve.remove(i-1)
            continue

            
    print(have)
    return have

n = 5
lost = [2, 4]
reserve = [1,3,5]

solution(n, lost, reserve)